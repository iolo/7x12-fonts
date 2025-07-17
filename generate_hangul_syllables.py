#!/usr/bin/fontforge -script

import fontforge
import sys

name = sys.argv[1]

f = fontforge.open('temp.ttf')

NUM_CHO = 19
NUM_JUNG = 21
NUM_JONG = 27

# 초성3벌, 중성1벌, 종성1벌
CHO_KIND = 3
JUNG_KIND = 1
JONG_KIND = 1

# 유니코드 첫가끝 초성/중성/종성
JAMO_CHO = 0x1100
JAMO_JUNG = 0x1161
JAMO_JONG = 0x11a8

# 유니코드 가~힣
KOR = 0xac00

# PUA(0xe000~0xf8ff) 영역에 조합용 한글 초성/중성/종성 글립이 들어있음
#PUA = 0xe010
# conflict with nerd font glyphs
# https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points
PUA = 0xf600

# 초성 글립
PUA_CHO = PUA
# 중성 글립
PUA_JUNG = PUA_CHO + NUM_CHO * CHO_KIND
# 종성 글립
PUA_JONG = PUA_JUNG + NUM_JUNG * JUNG_KIND

# 조합 규칙
# 종성에 따라 초성 결정
#                   ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
cho_kind_by_jung = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 0];

# 첫가끝 초성
code = JAMO_CHO
for cho in range(NUM_CHO):
    c = f.createChar(code)
    #print(f'cho={cho}->code={code:04x},char={chr(code)}')
    c.addReference(fontforge.nameFromUnicode(PUA_CHO + cho))
    code += 1

# 첫가끝 중성
code = JAMO_JUNG
for jung in range(NUM_JUNG):
    c = f.createChar(code)
    #print(f'jung={jung}->code={code:04x},char={chr(code)}')
    c.addReference(fontforge.nameFromUnicode(PUA_JUNG + jung))
    code += 1

# 첫가끝 종성
code = JAMO_JONG
for jong in range(NUM_JONG):
    c = f.createChar(code)
    #print(f'jong={jong}->code={code:04x},char={chr(code)}')
    c.addReference(fontforge.nameFromUnicode(PUA_JONG + jong))
    code += 1

code = KOR
for cho in range(NUM_CHO):
    for jung in range(NUM_JUNG):
        # 종성없음
        cho_kind = cho_kind_by_jung[jung];
        jung_kind = 0
        jong_kind = 0
        cho_code = PUA_CHO + NUM_CHO * cho_kind + cho
        jung_code = PUA_JUNG + NUM_JUNG * jung_kind + jung
        #print(f'cho={cho},jung={jung},jong={jong}->code={code:04x},char={chr(code)}')
        c = f.createChar(code)
        c.addReference(fontforge.nameFromUnicode(cho_code))
        c.addReference(fontforge.nameFromUnicode(jung_code))
        code += 1
        # 종성있음
        for jong in range(NUM_JONG):
            cho_kind = cho_kind_by_jung[jung];
            jung_kind = 0
            jong_kind = 0
            cho_code = PUA_CHO + NUM_CHO * cho_kind + cho
            jung_code = PUA_JUNG + NUM_JUNG * jung_kind + jung
            jong_code = PUA_JONG + NUM_JONG * jong_kind + jong
            #print(f'cho={cho},jung={jung},jong={jong}->code={code:04x},char={chr(code)}')
            c = f.createChar(code)
            c.addReference(fontforge.nameFromUnicode(cho_code))
            c.addReference(fontforge.nameFromUnicode(jung_code))
            c.addReference(fontforge.nameFromUnicode(jong_code))
            code += 1

f.os2_version = 4
f.os2_family_class = 49
f.os2_codepages = (0x00200000, 0x00000000)
f.os2_unicoderanges = (0x10000001, 0x11000000, 0x00000000, 0x00000000)

f.generate(f'{name}.ttf', flags=('short-post'))
f.generate(f'{name}.otf', flags=('short-post'))
f.generate(f'{name}.woff')
f.generate(f'{name}.woff2')

