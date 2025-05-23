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

bitsnpicas convertbitmap -f ttf -o temp.ttf 7x12.kbitx
fontforge --lang=py --script generate_hangul_syllables.py 7x12
rm temp.ttf

bitsnpicas convertbitmap -f ttf -o temp.ttf 7x12x3.kbitx
fontforge --lang=py --script generate_hangul_syllables.py 7x12x3
rm temp.ttf

bitsnpicas convertbitmap -f ttf -o temp.ttf 7x12-bold.kbitx
fontforge --lang=py --script generate_hangul_syllables.py 7x12-bold
rm temp.ttf
