movie thumbnailer (mtn)
http://moviethumbnail.sourceforge.net/

mtn was originaly developed by tuit (tuitfun); though most of its magic is actually done 
by FFmpeg libraries. For documents, please see in the doc directory and at
http://sourceforge.net/forum/?group_id=201133 .


====  Linux  ====

    == Dependency ==
     - ffmpeg
     - gd

    Fedora 25:
        $dnf install ffmpeg-devel gd-devel
    Ubuntu 17.4
        $sudo apt-get install libgd-dev libavutil-dev libavcodec-dev libavformat-dev libswscale-dev


    == Build ==
    $make

    == Install ==
    $su -c 'make install'


==== Windows ====

    == Dependency ==
     - MinGW    (http://www.mingw.org/)
     - ffmpeg   (http://www.ffmpeg.org)
     - gd       (https://libgd.github.io, libraries: http://gnuwin32.sourceforge.net/downlinks/gd-dep-zip.php)


    == Build ==
    1. update paths in Make.MinGW.bat
    2. run Make.MinGW.bat
