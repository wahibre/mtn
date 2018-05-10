movie thumbnailer (mtn)
fork from http://moviethumbnail.sourceforge.net/

mtn was originaly developed by tuit (tuitfun); though most of its magic is actually done 
by FFmpeg libraries. For documents, please see in the doc directory and at
https://gitlab.com/movie_thumbnailer/mtn/wikis/home .


Dependency
==========
 - ffmpeg   (>=3.1)
 - gd       (>=2.1.1)


Linux
=====

Build dependencies:

**Fedora** (with repo [RPMFUSION-FREE](https://rpmfusion.org/Configuration/) enabled)

    $dnf install ffmpeg-devel gd-devel

**Ubuntu, Debian**

    $sudo apt-get install libgd-dev libavutil-dev libavcodec-dev libavformat-dev libswscale-dev  

**FreeBSD**

    $pkg install gmake ffmpeg libgd


Build
-----
    $make

Install
-------
    $su -c 'make install'


Windows
=======

Build
-----
1. update paths in Make.MinGW.bat
2. run Make.MinGW.bat


References
==========
 * [FFmpeg project](http://www.ffmpeg.org)
 * [libgd project](https://libgd.github.io)
 * [libgd library and dependecies](http://gnuwin32.sourceforge.net/packages/gd.htm)
 * [MinGW](http://www.mingw.org/)
 * [RPM Fusion repository](https://rpmfusion.org/)
