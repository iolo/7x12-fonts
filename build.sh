#!/bin/bash

set -x

rm *.ttf *.sfd *.woff *.woff2

bitsnpicas.sh convertbitmap -f ttf -o 7x12.ttf 7x12.kbitx
fontforge -lang=ff -c 'Open($1); Save($2)' 7x12.ttf temp.sfd
node generate_hangul_syllables.mjs temp.sfd > 7x12.sfd
rm temp.sfd
fontforge -lang=ff -c 'Open($1); Generate($2)' 7x12.sfd 7x12.ttf
fonttools ttLib --flavor woff -o 7x12.woff 7x12.ttf
fonttools ttLib --flavor woff2 -o 7x12.woff2 7x12.ttf

bitsnpicas.sh convertbitmap -f ttf -o 7x12x3.ttf 7x12x3.kbitx
fontforge -lang=ff -c 'Open($1); Save($2)' 7x12x3.ttf temp.sfd
node generate_hangul_syllables.mjs temp.sfd > 7x12x3.sfd
rm temp.sfd
fontforge -lang=ff -c 'Open($1); Generate($2)' 7x12x3.sfd 7x12x3.ttf
fonttools ttLib --flavor woff -o 7x12x3.woff 7x12x3.ttf
fonttools ttLib --flavor woff2 -o 7x12x3.woff2 7x12x3.ttf
