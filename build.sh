#!/bin/bash

function exec_fontforge {
    fontforge $@
}

function exec_bitsnpicas {
    java -jar ./BitsNPicas.jar $@
}

function buildFont {
    rm "./fonts/$1*"
    exec_bitsnpicas convertbitmap -f ttf -o temp.ttf "src/$1.kbitx"
    exec_fontforge --lang=py --script generate_hangul_syllables.py "fonts/$1"
    if [ -x "./FontPatcher/font-patcher" ]; then
      exec_fontforge --lang=py --script ./FontPatcher/font-patcher --complete --out fonts "fonts/$1.ttf"
    fi
    rm temp.ttf
}

buildFont "7x12"
buildFont "5x12"
