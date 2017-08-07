#!/bin/bash

MTN=../src/mtn
VIDEO1=/media/zdielane/video/video.mp4
VIDEO2=/media/zdielane/video/The.Rover.2014.720p.BluRay.x264.YIFY.mp4
VIDEO2CH=/media/zdielane/video/7.\ Harry\ Potter\ and\ the\ Deathly\ Hallows\ Part-1\(Dual\ ITA-ENG\).DHILLON.mkv
O_DIR=output
FONT=DejaVuSans.ttf
MINSWIT="-f $FONT -O $O_DIR"


function colouredecho {
    echo -e '\e[0;32m'$1'\e[0m'
}


if [ ! -f $MTN ]; then
    echo "mtn not built!"
    exit
fi

rm -rf $O_DIR
mkdir -p $O_DIR

function run_test {

    case $1 in
    #---------------------------------------------------------
    1)
        colouredecho "====> Minimum switches"
        CMD="$MTN -o _minimum.jpg -f $FONT -O $O_DIR $VIDEO1"
    ;;
    #---------------------------------------------------------
    2)
        colouredecho "===> -X : use full input filename (include extension)"
        CMD="$MTN -X -g 3 -c 3 -r 4 -o _incl_ext.jpg -f $FONT -O $O_DIR $VIDEO2"
        ;;
    #---------------------------------------------------------
    3)
        colouredecho "===> -I : save individual shots too"
        CMD="$MTN -I -o _individ.jpg -f $FONT -O $O_DIR $VIDEO1"
        ;;
    #---------------------------------------------------------
    4)
        colouredecho "====> Verbose"
        CMD="$MTN -v -o _minimum.jpg -f $FONT -O $O_DIR $VIDEO1"
    ;;
    #---------------------------------------------------------
    5)
        colouredecho "===> dual audio channel"
        CMD="$MTN -o _dualaudio.jpg $MINSWIT $VIDEO2CH"
        ;;
    #---------------------------------------------------------
    *)
        exit
    esac

    echo $CMD
    $CMD

}

if [ -z "$1" ]; then
    for i in `seq 1 4`
    do
        run_test $i
    done
else
    run_test $1
fi
