Function exec_fontforge {
    & "${env:ProgramFiles(x86)}\FontForgeBuilds\fontforge.bat" $args
}

Function exec_bitsnpicas {
    & "${env:JAVA_HOME}\bin\java.exe" -jar "$HOME\apps\bitsnpicas\BitsNPicas.jar" $args
}

Function buildFont($name) {
    rm "./fonts/$name*"
    exec_bitsnpicas convertbitmap -f ttf -o temp.ttf "fonts/$name.bdf"
    exec_fontforge --lang=py --script generate_hangul_syllables.py "fonts/$name"
    if (Test-Path "./FontPatcher/font-patcher") {
      fontforge --lang=py --script ./FontPatcher/font-patcher --complete --out fonts "fonts/$name.ttf"
    }
    rm temp.ttf
}

buildFont "7x12"
buildFont "7x12x3"
buildFont "7x12-bold"
buildFont "7x12x3-bold"
