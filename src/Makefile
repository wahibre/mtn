#CFLAGS=-W -Wall -O3 -s -D_FILE_OFFSET_BITS=64 -mtune=i686 -march=i386 -I/home/tuitfun/include -L/home/tuitfun/lib
#CFLAGS=-W -Wall `pkg-config --cflags libavformat`
CFLAGS=-W -Wall
INCPATH=-I/usr/include/ffmpeg
DEBUGFLAG=-g
DESTDIR=
#LDFLAGS= -lavcodec -lavformat -lavcodec -lswscale -lavutil -lgd -lfreetype -ljpeg -lz -lm -lpthread
LIBS=-L/usr/lib64/ffmpeg -lavcodec -lavformat -lswscale -lavutil -lm -lgd

mtn: mtn.c Makefile
	 $(CC) -o mtn mtn.c $(INCPATH) $(CFLAGS) $(LDFLAGS) $(LIBS)
all: mtn mtns

mtns: mtn.c
	$(CC) -o mtns mtn.c -static $(INCPATH) $(CFLAGS) $(LDFLAGS) $(LIBS)

mtnd: mtn.c
	$(CC) -o mtn mtn.c $(INCPATH) $(CFLAGS) $(DEBUGFLAG) $(LDFLAGS) $(LIBS)

clean:
	rm -f mtn mtns

rebuild: clean mtn

install: mtn
	mkdir -p $(DESTDIR)/usr/bin/
	install -m 755 mtn $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/usr/share/doc/mtn
	cp -Rp ../doc/* $(DESTDIR)/usr/share/doc/mtn
	cp -p ../gpl-2.0.txt $(DESTDIR)/usr/share/doc/mtn

uninstall:
	rm -f  $(DESTDIR)/usr/bin/mtn
	rm -rf $(DESTDIR)/usr/share/doc/mtn
