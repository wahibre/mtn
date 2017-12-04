movie thumbnailer (mtn)
fork from http://moviethumbnail.sourceforge.net/

mtn was originaly developed by tuit (tuitfun); though most of its magic is actually done 
by FFmpeg libraries. For documents, please see in the doc directory and at
https://gitlab.com/movie_thumbnailer/mtn/wikis/home .


Dependency
==========
 - ffmpeg   (>=3.1)
 - gd       (>=2.2.4)


Linux
=====

Install dependency:  

**Fedora** 25,26 (with repo [RPMFUSION-FREE](https://rpmfusion.org/Configuration/) enabled)

    $dnf install ffmpeg-devel gd-devel

**Ubuntu** 17.4, **Debian** 9.1

    $sudo apt-get install libgd-dev libavutil-dev libavcodec-dev libavformat-dev libswscale-dev  


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
