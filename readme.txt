movie thumbnailer (mtn)
http://moviethumbnail.sourceforge.net/

mtn was originaly developed by tuit (tuitfun); though most of its magic is actually done 
by FFmpeg libraries. For documents, please see in the doc directory and at
http://sourceforge.net/forum/?group_id=201133 .


Dependency:
 - ffmpeg
 - gd

Fedora 25:
$dnf install ffmpeg-devel gd-devel


Build:
$make

Install:
$make install
