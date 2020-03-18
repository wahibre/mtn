@echo off

REM 1. Install MinGW:
REM
REM - Download mingw-get-setup.exe from https://sourceforge.net/projects/mingw/files/Installer/
REM - mingw-get-setup.exe first installs its bare version to C:\MinGW
REM - After that a new window titled "MinGW Installation Manager" appears where more packages can be installed/updated.
REM - In that second window select "All Packages" in the left pane, then scroll in the right pane to the line with Package "mingw32-gcc" and Class "bin" and mark its checkbox.
REM - Finally click "Installation" in the top menu and do "apply changes"
REM
REM
REM 2. Install FFmpeg and libGD:
REM
REM - Download the dependency ZIP files:
REM     - FFmpeg (choose prefered version)
REM         from https://ffmpeg.zeranoe.com/builds/win32/shared/
REM          and https://ffmpeg.zeranoe.com/builds/win32/dev/
REM     - libGD (Binaries, Dependencies and Developer files)
REM         from http://gnuwin32.sourceforge.net/packages/gd.htm
REM - Unzip all of the files into the folder C:\MinGW which the MinGW installer has already created.
REM - Verify that you unzipped the files correctly. For example the dependency gd-2.0.33-1-dep.zip contains the file \bin\libpng13.dll.
REM   If you unzipped correctly that file should now be at C:\MinGW\bin\libpng13.dll
REM
REM   dependent libraries are now located here:
REM   (note: numbered suffix depends on FFmpeg version)
REM     c:\MinGW\bin\AVCODEC-58.DLL
REM     c:\MinGW\bin\AVFORMAT-58.DLL
REM     c:\MinGW\bin\AVUTIL-56.DLL
REM     c:\MinGW\bin\FREETYPE6.DLL
REM     c:\MinGW\bin\JPEG62.DLL
REM     c:\MinGW\bin\LIBGD2.DLL
REM     c:\MinGW\bin\LIBICONV2.DLL
REM     c:\MinGW\bin\LIBPNG13.DLL
REM     c:\MinGW\bin\SWRESAMPLE-3.DLL
REM     c:\MinGW\bin\SWSCALE-5.DLL
REM     c:\MinGW\bin\ZLIB1.DLL
REM
REM 3. Build MTN by running this script
REM    C:\..\mtn\src> Make.MinGW.bat
REM
REM 4. To run MTN you need 
REM    - either add "c:\MinGW\bin" to your PATH environment variable
REM    - or copy dependent libraries from C:\MinGW\bin and place in the same folder as mtn.exe



set PATH=c:\MinGW\bin;%PATH%

set CC=gcc
set CFLAGS=-Wall -DWIN32 -O3

set LDFLAGS=-Lc:\MinGW\lib
set INCLUDE=-Ic:\MinGW\include
set LIBS=-lgd -lavutil -lavdevice -lavformat -lavcodec  -lswscale

%CC% -o mtn mtn.c %CFLAGS% %LDFLAGS% %INCLUDE% %LIBS%
