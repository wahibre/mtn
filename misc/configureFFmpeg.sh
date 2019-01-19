#!/usr/bin/bash

./configure   \
--pkg-config-flags="--static" \
--disable-alsa \
--disable-avdevice \
--disable-avfilter \
--disable-bsfs \
--disable-doc \
--disable-encoders \
--disable-filters \
--disable-indevs \
--disable-muxers \
--disable-network \
--disable-outdevs \
--disable-parsers \
--disable-postproc \
--disable-programs \
--disable-shared \
--disable-swresample \
--disable-x86asm \
--disable-autodetect \

exit

--disable-protocols \
--disable-demuxers \
--disable-bzlib \
--disable-iconv \
--disable-libxcb \
--disable-libxcb-shape \
--disable-libxcb-shm \
--disable-libxcb-xfixes \
--disable-xlib \
--disable-zlib \
--disable-fft     \
--disable-faan    \
--disable-dct     \
--disable-dwt     \
--disable-lsp     \
--disable-lzo     \
--disable-mdct    \
--disable-rdft    \
--enable-gpl \
--enable-parser=h264
--enable-libx264 \
--enable-libx265 \
--enable-libxvid \
--enable-libzvbi \
