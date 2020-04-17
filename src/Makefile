#CFLAGS=-W -Wall -O3 -s -D_FILE_OFFSET_BITS=64 -mtune=i686 -march=i386 -I/home/tuitfun/include -L/home/tuitfun/lib
#CFLAGS=-W -Wall `pkg-config --cflags libavformat`

# The DESTDIR is macro is used for staged builds, so that it gets installed
# under a fake root directory for the sake of packaging. Unlike PREFIX, it will
# not actually be run from this directory.
#DESTDIR - reserved for rpmbuild

# According to a convention, PREFIX macro is the prefix of instalation.
PREFIX = /usr/local

UNAME=$(shell uname -s)
CFLAGS=-W -Wall -O3 $(USER_CFLAGS)
OUT=../bin
LIBSDIR=../lib

ifeq ($(UNAME),FreeBSD)
LIBS+=-L/usr/local/lib
INCPATH+=-I/usr/local/include
endif

ifeq ($(UNAME),Linux)
INCPATH=-I/usr/include/ffmpeg
endif

LIBS+=-lavcodec -lavformat -lavcodec -lswscale -lavutil -lgd -lfreetype -ljpeg -lz -lm -lpthread
S_INCPATH=-I$(LIBSDIR)/FFmpeg -I$(LIBSDIR)/libgd/src
S_LIBS= -static-libgcc -static \
	$(LIBSDIR)/FFmpeg/libavformat/libavformat.a \
	$(LIBSDIR)/FFmpeg/libavcodec/libavcodec.a \
	$(LIBSDIR)/FFmpeg/libswscale/libswscale.a \
	$(LIBSDIR)/FFmpeg/libavutil/libavutil.a \
	$(LIBSDIR)/libgd/Bin/libgd.a \
	-lpthread -lbz2 -lfreetype -ljpeg -lpng16 -lz -lm

mtn: mtn.c outdir
	$(CC) -o $(OUT)/mtn mtn.c $(INCPATH) $(CFLAGS) $(LIBS)

outdir:
	mkdir -p $(OUT)

mtns: mtn.c outdir
	$(CC) -o $(OUT)/mtn mtn.c $(S_INCPATH) $(CFLAGS) $(S_LIBS)

mtnd: mtn.c outdir
	$(CC) -o $(OUT)/mtn mtn.c $(INCPATH) -W -Wall -g $(LIBS)

clean:
	rm -f $(OUT)/mtn

distclean:
	rm -rf $(OUT)

rebuild:  clean mtn
rebuilds: clean mtns

test_bin:
	$(OUT)/mtn -f ../test/font.ttf -O /tmp /home/sample.avi
	test -s /tmp/sample_s.jpg

test:  rebuild  mtn  test_bin
tests: rebuilds mtns test_bin

install: mtn
	mkdir -p $(DESTDIR)$(PREFIX)/bin/
	install -m 755 $(OUT)/mtn $(DESTDIR)$(PREFIX)/bin/
	mkdir -p $(DESTDIR)$(PREFIX)/share/doc/mtn
	cp -Rp ../doc/* $(DESTDIR)$(PREFIX)/share/doc/mtn
	cp -p ../gpl-2.0.txt $(DESTDIR)$(PREFIX)/share/doc/mtn
	mkdir -p $(DESTDIR)$(PREFIX)/share/man/man1
	cp -p ../man/mtn.1 $(DESTDIR)$(PREFIX)/share/man/man1/

uninstall:
	rm -f  $(DESTDIR)$(PREFIX)/share/man/man1/mtn.1
	rm -f  $(DESTDIR)$(PREFIX)/bin/mtn
	rm -rf $(DESTDIR)$(PREFIX)/share/doc/mtn

