Function fontforge {
    & "${env:ProgramFiles(x86)}\FontForgeBuilds\fontforge.bat" $args
}

Function bitsnpicas {
    & "${env:JAVA_HOME}\bin\java.exe" -jar "$HOME\apps\bitsnpicas\BitsNPicas.jar" $args
}

rm *.sfd
rm *.ttf
rm *.otf
rm *.woff
rm *.woff2

bitsnpicas convertbitmap -f ttf -o test.ttf 7x12.kbitx
fontforge --lang=py --script generate_hangul_syllables.py
mv test2.otf 7x12.otf
mv test2.ttf 7x12.ttf
mv test2.woff 7x12.woff
mv test2.woff2 7x12.woff2
rm test.ttf

bitsnpicas convertbitmap -f ttf -o test.ttf 7x12x3.kbitx
fontforge --lang=py --script generate_hangul_syllables.py
mv test2.otf 7x12x3.otf
mv test2.ttf 7x12x3.ttf
mv test2.woff 7x12x3.woff
mv test2.woff2 7x12x3.woff2
rm test.ttf
