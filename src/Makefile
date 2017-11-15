#CFLAGS=-W -Wall -O3 -s -D_FILE_OFFSET_BITS=64 -mtune=i686 -march=i386 -I/home/tuitfun/include -L/home/tuitfun/lib
#CFLAGS=-W -Wall `pkg-config --cflags libavformat`

CFLAGS=-W -Wall
INCPATH=-I/usr/include/ffmpeg
#DESTDIR - reserved for rpmbuild
OUT=../bin
LIBSDIR=../lib
LIBS=-lavcodec -lavformat -lavcodec -lswscale -lavutil -lgd -lfreetype -ljpeg -lz -lm -lpthread
S_INCPATH=-I$(LIBSDIR)/FFmpeg -I$(LIBSDIR)/libgd/src
S_LIBS=$(LIBSDIR)/libpng.a $(LIBSDIR)/libgd.a $(LIBSDIR)/libavformat.a $(LIBSDIR)/libavcodec.a $(LIBSDIR)/libswscale.a $(LIBSDIR)/libavutil.a $(LIBSDIR)/libz.a \
-lm -lpthread -lbz2 -ldl -ljpeg -lfreetype

mtn: mtn.c outdir
	 $(CC) -o $(OUT)/mtn mtn.c $(INCPATH) $(CFLAGS) $(LIBS)

outdir:
	mkdir -p $(OUT)

mtns: mtn.c outdir
	$(CC) -o $(OUT)/mtn mtn.c $(S_INCPATH) $(CFLAGS) $(S_LIBS)

mtnd: mtn.c outdir
	$(CC) -o $(OUT)/mtn mtn.c $(INCPATH) $(CFLAGS) -g $(LIBS)

clean:
	rm -f $(OUT)/mtn

distclean:
	rm -rf $(OUT)

rebuild:  clean mtn
rebuilds: clean mtns

test_bin:
	$(OUT)/mtn -f /usr/share/fonts/aajohan-comfortaa/Comfortaa-Regular.ttf -O /tmp /home/sample.avi
	test -e /tmp/sample_s.jpg

test:  rebuild  mtn  test_bin
tests: rebuilds mtns test_bin

install: mtn
	mkdir -p $(DESTDIR)/usr/bin/
	install -m 755 $(OUT)/mtn $(DESTDIR)/usr/bin/
	mkdir -p $(DESTDIR)/usr/share/doc/mtn
	cp -Rp ../doc/* $(DESTDIR)/usr/share/doc/mtn
	cp -p ../gpl-2.0.txt $(DESTDIR)/usr/share/doc/mtn

uninstall:
	rm -f  $(DESTDIR)/usr/bin/mtn
	rm -rf $(DESTDIR)/usr/share/doc/mtn
