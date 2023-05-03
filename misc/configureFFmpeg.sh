#!/usr/bin/bash

./configure   \
--pkg-config-flags="--static" \
--disable-alsa \
--disable-avdevice \
--disable-bsfs \
--disable-doc \
--disable-encoders \
--disable-indevs \
--disable-muxers \
--disable-network \
--disable-outdevs \
--disable-parsers \
--disable-postproc \
--disable-programs \
--disable-shared \
--disable-x86asm \
--disable-autodetect
