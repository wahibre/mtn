#!/bin/bash -e

# Purpose of this skript is to test most of posible MTN options

# Usage:
#    run_mtn.sh [FILE_OR_DIR]
# 
# Env. variable: 
#    MTN - path to the binary (for overriding)


export LANG=en_US
VID_COVER=""
VID_UTF=""
VID_HDR=""
VID_DIR=""
FONT_UTF=""
FONT="$(dirname $(readlink -f "$0"))/font.ttf"

[ -v ${MTN} ] && MTN=$(which mtn)

# VIDEO have to be a full path
if [ -n "$1" ]; then
    VIDEO="$1"
else
    VIDEO="$(pwd)"
fi

if [ ! -f $MTN ]; then
    echo "mtn not built!"
    exit 1
fi

if [ ! -f $FONT ]; then
    echo "cant find test font!"
    exit 1
fi

function colouredecho {
    echo -e '\e[0;32m'$1'\e[0m'
}

function run_mtn {
    pushd $O_DIR > /dev/null
    CMD="$MTN $MIN_SWITCHES $*"
    echo $CMD $VIDEO
    $CMD "$VIDEO" &>>out.log
    popd > /dev/null
}

function tcdir {
    ((testcasenr++))
    O_DIR="${testcasenr}_$1"
    mkdir -p "$O_DIR"
}

testcasenr=0
SCREENS_DIR=screenshots
MIN_SWITCHES="-O . "

rm -rf $SCREENS_DIR
mkdir -p $SCREENS_DIR
cd $SCREENS_DIR

colouredecho "====> Minimum switches"
tcdir minimum
run_mtn

colouredecho "====> Use full input filename (include extension)"
tcdir filename_extension_nosuffix
run_mtn -X -o .jpg

colouredecho  "===> Save individual shots (small and large) only"
tcdir individual_shots
run_mtn -c2 -r1 -I toi

colouredecho  "===> Save image to avif"
tcdir avif
run_mtn -o .avif

colouredecho  "===> Save image to webp"
tcdir webp
run_mtn -o .webp

colouredecho  "===> Transparent png image"
tcdir transparent_png_noinfo
run_mtn -o .png --transparent -i -g 10 -k 00FFBB

colouredecho  "===> Fixed grid"
tcdir grid_3_3_with_cover
run_mtn -r3 -c3 --cover $VID_COVER

colouredecho  "===> Info in text file"
tcdir info_in_file
run_mtn -i -N _info.txt

colouredecho  "===> Verbose"
tcdir seeking_verbose
run_mtn -z -v

colouredecho  "===> Override aspect ratio 4:3"
tcdir aspect_4_3
run_mtn -a 1.3333

colouredecho  "===> Process 30s length with nonseek"
tcdir lenght_30s
run_mtn -b 1 -D 0 -s 2 -C 32 -Z

colouredecho  "===> Skip 5min. at the Beginning and End of file"
tcdir skip_ends_5min
run_mtn -B 300.01 -E 300.5

colouredecho  "===> Timestamp off "
tcdir timestamp_off_title_on
run_mtn -t -T timestamp-off

colouredecho  "===> Shadows "
tcdir shadows
run_mtn --shadow=5 -g 12 -o .png

colouredecho  "===> Colors & fonts, recursive "
tcdir colors
testfont="$FONT"
run_mtn -g 5 -k 10FF55 -f $testfont -F FF1010:16:$testfont:FFFFFF:FF0000:20 -d 1

colouredecho  "===> Text position "
tcdir text_position_changed
run_mtn -k FFFFFF -g 5 -L 3:4

colouredecho  "===> First stream, one shot full width"
tcdir firt_stream_one_shot
run_mtn -c1 -r1 -w0 -S 0

colouredecho  "===> Low quality jpeg, human readable size, quietly"
tcdir low_quality_human_size_quietly
run_mtn -j 30 -q -H

colouredecho  "===> Tall shots"
tcdir tall_shots
run_mtn -C 30 -h 300

colouredecho  "===> Custom filename"
tcdir custom_filename
run_mtn -r2 -c2 -o .jpg -It -N.txt -x "MyCustomFileName"

colouredecho  "===> WebVTT"
tcdir webvtt
run_mtn -c 4 -w 1280 -Ii --vtt=path_to_image/

colouredecho  "===> Filters"
tcdir filters
run_mtn --filters='split[main][tmp];[tmp]crop=iw/2:ih:0:0,hflip[flip];[main][flip]overlay=W/2:0'

colouredecho  "===> Paused with normal priority"
tcdir normal_priority
run_mtn -c1 -r1 -p -n

unset VIDEO

colouredecho  "===> file extensions"
tcdir file_ext
run_mtn -e mp4 -r1 -c1 "$VID_DIR"

colouredecho  "===> unicode"
tcdir unicode
run_mtn -f $FONT_UTF -C 20 "$VID_UTF"

colouredecho  "===> tonemap"
tcdir tonemap
run_mtn -C 95 -D0 -b2 "$VID_HDR"
run_mtn -C 95 -D0 -b2 --tonemap -o_tonemap.jpg "$VID_HDR"
