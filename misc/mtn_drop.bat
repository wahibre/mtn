@echo off
:: Drag and drop script
::
:: usage: Drag and drop one or more videos (or folders of videos) onto this
:: script (or a shortcut to it).
::
:: setup: Edit the start line below to reflect the location of mtn.exe on
:: your system and your chosen options.
:: Below that, you can also enable pause at finish (remove 'rem')

:: drag-drop code from dbenham
setlocal DisableDelayedExpansion
:: first assume normal call, get args from %*
set args=%*
set "dragDrop="
set MTN_EXE="C:\Program Files\mtn\mtn.exe"
::
:: Now check if drag&drop situation by looking for %0 in !cmdcmdline!
:: if found then set drag&drop flag and get args from !cmdcmdline!
setlocal EnableDelayedExpansion
set "cmd=!cmdcmdline!"
set "cmd2=!cmd:*%~f0=!"
if "!cmd2!" neq "!cmd!" (
  set dragDrop=1
  set "args=!cmd2:~0,-1! "
  set "args=!args:* =!"
)
::
:: Process the args
for %%F in (!args!) do (
  if "!!"=="" endlocal & set "dragDrop=%dragDrop%"
  rem ------------------------------------------------
  rem - Your file processing starts here.
  rem - Each file will be processed one at a time
  rem - The file path will be in %%F
  rem -

  echo Process file "%%~F"

rem ====================================
rem  Start mtn here.
rem  'start' command priorities: /low /normal /high /realtime /abovenormal /belownormal

start "movie thumbnailer" /b /belownormal /wait %MTN_EXE% -P -h 0 -c 3 -r 4 -w 1280 -g 1 -j 92 -D 12 -L 4:2 -k ffffff -f arial.ttf -F 000000:12:arial.ttf:ffffff:000000:12 "%%~F"

  rem -
  rem - Your file processing ends here
  rem -------------------------------------------------
)
::
:: If drag&drop then must do a hard exit to prevent unwanted execution
:: of any split drag&drop filename argument
if defined dragDrop (
rem  pause
  exit
)
