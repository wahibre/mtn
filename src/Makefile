#CFLAGS=-W -Wall -O3 -s -D_FILE_OFFSET_BITS=64 -mtune=i686 -march=i386 -I/home/tuitfun/include -L/home/tuitfun/lib
#CFLAGS=-W -Wall `pkg-config --cflags libavformat`
CFLAGS=-W -Wall
INCPATH=-I/usr/include/ffmpeg
#LDFLAGS= -lavcodec -lavformat -lavcodec -lswscale -lavutil -lgd -lfreetype -ljpeg -lz -lm -lpthread
LIBS=-L/usr/lib64/ffmpeg -lavcodec -lavformat -lswscale -lavutil -lm -lgd

mtn: mtn.c Makefile
	$(CC) -o mtn mtn.c         $(INCPATH) $(CFLAGS) $(LDFLAGS) $(LIBS)

all: mtn mtns

mtns: mtn.c
	$(CC) -o mtns mtn.c -static $(INCPATH) $(CFLAGS) $(LDFLAGS) $(LIBS)

clean:
	rm -f mtn mtns

rebuild: clean mtn

install: mtn
	install -o root -g root -m 755 mtn /usr/bin/
