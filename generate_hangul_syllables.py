import fontforge

f = fontforge.open("test.ttf")

NUM_CHO = 19
NUM_JUNG = 21
NUM_JONG = 28 # filler + 27

CHO_KIND = 3
JUNG_KIND = 1
JONG_KIND = 1

# 가~힣
KOR = 0xac00;
# PUA 영역에 조합용 한글 초성/중성/종성 글립이 들어있음
PUA = 0xe010;

CHO = PUA # 초성 글립(3종류)
JUNG = PUA + NUM_CHO * CHO_KIND # 중성 글립(1종류)
JONG = PUA + NUM_CHO * CHO_KIND + NUM_JUNG * JUNG_KIND # 종성 글립(1종류)

# 0=세로모음용 초성
# 1=가로모음용 초성
# 2=복모음용 초성
cho_kind_by_jung = [
# ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅗ,ㅘ,ㅙ,ㅚ,ㅛ,ㅜ,ㅝ,ㅞ,ㅟ,ㅠ,ㅡ,ㅢ,ㅣ
  0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 0,
]

code = KOR;
for cho in range(NUM_CHO):
    for jung in range(NUM_JUNG):
        cho_code = CHO + NUM_CHO * cho_kind_by_jung[jung] + cho
        jung_code = JUNG + jung
        for jong in range(NUM_JONG):
            jong_code = JONG + jong
            print(f'cho={cho},jung={jung},jong={jong}->code={code:04x},char={chr(code)}')
            c = f.createChar(code);
            c.addReference(fontforge.nameFromUnicode(cho_code))
            c.addReference(fontforge.nameFromUnicode(jung_code))
            c.addReference(fontforge.nameFromUnicode(jong_code))
            code += 1

#c2 = f.createChar(0xAC01);
#c2.addReference(fontforge.nameFromUnicode(0xE000));
#c2.addReference(fontforge.nameFromUnicode(0xE039));
#c2.addReference(fontforge.nameFromUnicode(0xE04F));

# f.selection.select(0xE000, 0xE039)
# f.copyReference()
# f.createChar(0xAC00);
# f.selection.select(0xAC00);
# f.paste();

# f.selection.select(0xE000, 0xE039, 0xE04F)
# f.copyReference()
# f.createChar(0xAC01);
# f.selection.select(0xAC01);
# f.paste();

f.os2_version = 4;
f.generate("test2.otf")
f.generate("test2.ttf")
f.generate("test2.woff")
f.generate("test2.woff2")

