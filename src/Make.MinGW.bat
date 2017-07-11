@echo off

REM First update paths to your locations


set PATH=c:\MinGW\bin;%PATH%

set CC=gcc
set CFLAGS=-Wall -DWIN32 -static -O3
set LDFLAGS=-Lc:\MinGW\lib
set INCLUDE=-Ic:\MinGW\include
set LIBS=-llibgd -lavutil -lavdevice -lavformat -lavcodec  -lswscale -lm

%CC% -o mtn mtn.c %CFLAGS% %LDFLAGS% %INCLUDE% %LIBS%
