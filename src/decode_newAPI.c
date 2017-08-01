#ifdef WIN32
    #define UNICODE
    #define _UNICODE
#endif

#include <assert.h>
#include <ctype.h>
#include <dirent.h>
#include <errno.h>
#include <fcntl.h>
#include <locale.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>

#include "libavutil/imgutils.h"
#include "libavutil/avutil.h"
#include "libavcodec/avcodec.h"
#include "libavformat/avformat.h"
#include "libswscale/swscale.h"

#include "gd.h"



#define LOG_INFO 0

/**
 * Convert an error code into a text message.
 * @param error Error code to be converted
 * @return Corresponding error text (not thread-safe)
 */
static const char *get_error_text(const int error)
{
    static char error_buffer[255];
    av_strerror(error, error_buffer, sizeof(error_buffer));
    return error_buffer;
}
static void pgm_save(unsigned char *buf, int linesize, int xsize, int ysize,
                     char *filename)
{
    FILE *f;
    int i;

    f = fopen(filename,"w");
    fprintf(f, "P5\n%d %d\n%d\n", xsize, ysize, 255);
    for (i = 0; i < ysize; i++)
        fwrite(buf + i * linesize, 1, xsize, f);
    fclose(f);
}





static void decode(AVCodecContext *dec_ctx, AVFrame *frame, AVPacket *pkt,
                   const char *filename)
{
    char buf[1024];
    int ret;

    ret = avcodec_send_packet(dec_ctx, pkt);
    if (ret < 0) {
        av_log(NULL, AV_LOG_ERROR,  "Error sending a packet for decoding - %s\n", get_error_text(ret));
        exit(1);
    }

    while (ret >= 0) {
        ret = avcodec_receive_frame(dec_ctx, frame);
        if (ret == AVERROR(EAGAIN) )
        {
            av_log(NULL, AV_LOG_ERROR, "recieved AVERROR(EAGAIN)\n");
            return;
        }
        if(ret == AVERROR_EOF)
        {
            av_log(NULL, AV_LOG_ERROR, "recieved AVERROR_EOF\n");
            return;
        }
        if (ret < 0) {
            av_log(NULL, AV_LOG_ERROR, "Error during decoding\n");
            exit(1);
        }


        /* the picture is allocated by the decoder. no need to free it */
        snprintf(buf, sizeof(buf), "%s-%d.pgm", filename, dec_ctx->frame_number%5); //TODO remove %5
        printf("saving frame %3d to %s\n", dec_ctx->frame_number, buf);

        fflush(stdout);
        pgm_save(frame->data[0], frame->linesize[0],
                 frame->width, frame->height, buf);
    }
}




int main(int __attribute__((unused)) argc, char __attribute__((unused)) *argv[])
{
    const char* filename = "/home/vm/Desktop/video.mp4";
//    const char* filename = "/media/zdielane/video/tdv-din.avi";

    AVFormatContext *pFormatCtx = NULL;
    AVCodecContext *input_codec_context = NULL;
    AVCodec *input_codec;
    AVCodecContext *avctx;
    AVPacket *pkt;
    AVFrame *frame;
    int video_stream_index, error;
    AVStream *pStream = NULL;


    /* init */
    av_register_all();          // Register all formats and codecs


    /** Open the input file to read from it. */
    if (avformat_open_input(&pFormatCtx, filename, NULL, NULL) < 0)
    {
        av_log(NULL, AV_LOG_ERROR, "open_input_file error\n");
        return 1;
    }


    /** Get information on the input file (number of streams etc.). */
    if ((error = avformat_find_stream_info(pFormatCtx, NULL)) < 0)
    {
        av_log(NULL, AV_LOG_ERROR, "avformat_find_stream_info error\n");
        return 2;
    }

    video_stream_index=-1;
    /** select video stream */
    for(uint i=0; i<pFormatCtx->nb_streams; i++)
    {
        if(pFormatCtx->streams[i]->codecpar->codec_type == AVMEDIA_TYPE_VIDEO )
        {
            video_stream_index = i;
            pStream = pFormatCtx->streams[i];
        }
    }

    /** Find a decoder for the audio stream. */
    if (!(input_codec = avcodec_find_decoder(pFormatCtx->streams[video_stream_index]->codecpar->codec_id)))
    {
        av_log(NULL, AV_LOG_ERROR, "avcodec_find_decoder error\n");
        return 3;
    }

    /** allocate a new decoding context */
    avctx = avcodec_alloc_context3(input_codec);
    if (!avctx) {
        av_log(NULL, AV_LOG_ERROR, "Could not allocate a decoding context\n");
        return 4;
    }

    /** initialize the stream parameters with demuxer information */
    error = avcodec_parameters_to_context(avctx, pFormatCtx->streams[0]->codecpar);
    if (error < 0) {
        av_log(NULL, AV_LOG_ERROR ,"Could not open input codec (error '%s')\n",  get_error_text(error));
        return 5;
    }

    /** Open the decoder for the audio stream to use it later. */
    if ((error = avcodec_open2(avctx, input_codec, NULL)) < 0) {
        av_log(NULL, AV_LOG_ERROR ,"Could not open input codec (error '%s')\n",  get_error_text(error));
        return 6;
    }


    pkt = av_packet_alloc();
    if (!pkt)
    {
        av_log(NULL, AV_LOG_ERROR ,"Could not allocate packet\n");
        return 6;
    }

    frame = av_frame_alloc();
    if (!frame) {
        av_log(NULL, AV_LOG_ERROR ,"Could not allocate video frame\n");
        return 10;
    }

//    avcodec_flush_buffers(avctx);

    if((error = av_seek_frame(pFormatCtx, video_stream_index, 50/av_q2d(pStream->time_base) , 0)) < 0)
    {
        av_log(NULL, AV_LOG_ERROR ,"Could not seek\n");
        return 11;
    }


    int fret;
    for (int j=0; j<12;j++)
    {
        do
        {
            av_packet_unref(pkt);
            fret = av_read_frame(pFormatCtx, pkt);
            if(pkt->stream_index != video_stream_index)
                fret=-1;

        } while(fret!=0);

        decode(avctx, frame, pkt, "/home/vm/Desktop/obr" /*filename*/);
    }


    /**
     * cleaning
    */

    if (input_codec_context)
        avcodec_free_context(&input_codec_context);
    if (pFormatCtx)
        avformat_close_input(&pFormatCtx);

    av_frame_free(&frame);
    av_packet_free(&pkt);
    av_free(pkt);
}
