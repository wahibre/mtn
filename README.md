Description
===========
movie thumbnailer (mtn)  
fork from http://moviethumbnail.sourceforge.net/  

Movie Thumbnailer (mtn) saves thumbnails (screenshots) of movie or video files to image files (jpg, png). 
It uses FFmpeg's libavcodec as its engine, so it supports all popular codecs, e.g. h.265/hevc, h.264, mpeg1, mpeg2, mp4, vc1, wmv, xvid, divx...     
mtn was originaly developed by tuit (tuitfun); though most of its magic is actually done 
by FFmpeg libraries. For documents, please see in the doc directory and at
https://gitlab.com/movie_thumbnailer/mtn/wikis/home .


Dependency
==========
 - ffmpeg   (>=3.1)
 - gd       (>=2.1.1)

Getting source
==============
    $git clone https://gitlab.com/movie_thumbnailer/mtn.git
    $cd mtn/src
    
Installing from source
======================

**Fedora** 

	$dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
    $dnf install ffmpeg-devel gd-devel make gcc-c++  
    $make
    $su -c 'make install'

**Ubuntu, Debian**

    $sudo apt-get install libgd-dev libavutil-dev libavcodec-dev libavformat-dev libswscale-dev make  
    $make
    $sudo make install

**Manjaro**  

    $pacman -S gd ffmpeg make gcc
    $make
    $su -c 'make install'

**OpenSUSE**  

*n/a*  
*FFmpeg >=3.1 not available

**CentOS**  

*n/a*  
*FFmpeg >=3.1 not available in RPMFusion repository*  

**Mint**  

*n/a*  
*FFmpeg >=3.1 not available in repository*  

**FreeBSD**

    $pkg install gmake ffmpeg libgd
    $gmake

**Windows**  

    c:\..\mtn\src> Make.MinGW.bat


References
==========
 * [FFmpeg project](http://www.ffmpeg.org)
 * [libgd project](https://libgd.github.io)
 * [libgd library and dependecies](http://gnuwin32.sourceforge.net/packages/gd.htm)
 * [MinGW](http://www.mingw.org/)
 * [RPM Fusion repository](https://rpmfusion.org/)
