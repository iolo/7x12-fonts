#!/usr/bin/fontforge -script

import fontforge

f = fontforge.open("test.ttf")

NUM_CHO = 19
NUM_JUNG = 21
NUM_JONG = 28 # filler + 27

CHO_KIND = 3
JUNG_KIND = 1
JONG_KIND = 1

# 자모 초성/중성/종성
JAMO_CHO = 0x1100
JAMO_JUNG = 0x1161
JAMO_JONG = 0x11a8

# 가~힣
KOR = 0xac00
# PUA 영역에 조합용 한글 초성/중성/종성 글립이 들어있음
PUA = 0xe010

PUA_CHO = PUA # 초성 글립(3종류)
PUA_JUNG = PUA_CHO + NUM_CHO * CHO_KIND # 중성 글립(1종류)
PUA_JONG = PUA_CHO + NUM_CHO * CHO_KIND + NUM_JUNG * JUNG_KIND # 종성 글립(1종류)

# 0=세로모음용 초성
# 1=가로모음용 초성
# 2=복모음용 초성
cho_kind_by_jung = [
# ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅗ,ㅘ,ㅙ,ㅚ,ㅛ,ㅜ,ㅝ,ㅞ,ㅟ,ㅠ,ㅡ,ㅢ,ㅣ
  0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 0,
]

code = JAMO_CHO
for cho in range(NUM_CHO):
    c = f.createChar(code)
    c.addReference(fontforge.nameFromUnicode(PUA_CHO + cho))
    code += 1

code = JAMO_JUNG
for jung in range(NUM_JUNG):
    c = f.createChar(code)
    c.addReference(fontforge.nameFromUnicode(PUA_JUNG + jung))
    code += 1

code = JAMO_JONG
for jong in range(NUM_JONG):
    c = f.createChar(code)
    c.addReference(fontforge.nameFromUnicode(PUA_JONG + jong))
    code += 1

code = KOR
for cho in range(NUM_CHO):
    for jung in range(NUM_JUNG):
        cho_code = PUA_CHO + NUM_CHO * cho_kind_by_jung[jung] + cho
        jung_code = PUA_JUNG + jung
        for jong in range(NUM_JONG):
            jong_code = PUA_JONG + jong
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

f.generate("test2.ttf")
f.generate("test2.otf")
f.generate("test2.woff")
f.generate("test2.woff2")

