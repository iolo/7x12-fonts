const NUM_CHO = 19;
const NUM_JUNG = 21;
const NUM_JONG = 28; // with filler

const CHO_KIND = 3;
const JUNG_KIND = 1;
const JONG_KIND = 1;

// 가~힣
const KOR = 0xac00;
// PUA 영역에 조합용 한글 초성/중성/종성 글립이 들어있음
const PUA = 0xe000;

// TODO: find GID from sfd file
// last GID + 1
const KOR_GID = 205;
// StartChar: uniE000
// Encoding: 57344 57344 99
const PUA_GID = 99;

const CHO = PUA; // 초성 글립(3종류)
const JUNG = PUA + NUM_CHO * CHO_KIND; // 중성 글립(1종류)
const JONG = PUA + NUM_CHO * CHO_KIND + NUM_JUNG * JUNG_KIND; // 종성 글립(1종류)

const CHO_GID = PUA_GID;
const JUNG_GID = PUA_GID + NUM_CHO * CHO_KIND;
const JONG_GID = PUA_GID + NUM_CHO * CHO_KIND + NUM_JUNG * JUNG_KIND;

// 0=세로모음용 초성
// 1=가로모음용 초성
// 2=복모음용 초성
const cho_kind_by_jung = [
//ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅗ,ㅘ,ㅙ,ㅚ,ㅛ,ㅜ,ㅝ,ㅞ,ㅟ,ㅠ,ㅡ,ㅢ,ㅣ
  0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 0,
];
const width = 1400; // 4000 for for 7x12x3

let code = KOR;
let gid = KOR_GID;
for (let cho = 0; cho < NUM_CHO; cho++) {
  for (let jung = 0; jung < NUM_JUNG; jung++) {
    const cho_index = NUM_CHO * cho_kind_by_jung[jung] + cho;
    const cho_code = CHO + cho_index;
    const cho_gid = CHO_GID + cho_index;
    const jung_code = JUNG + jung;
    const jung_gid = JUNG_GID + jung;
    for (let jong = 0; jong < NUM_JONG; jong++) {
      const jong_code = JONG + jong;
      const jong_gid = JONG_GID + jong;
      console.log(`StartChar: uni${Number(code).toString(16).toUpperCase()}
Encoding: ${code} ${code} ${gid}
Width: ${width}
Flags: W
LayerCount: 3
Fore`);
      console.log(`Refer: ${cho_gid} ${cho_code} N 1 0 0 1 0 0 2`);
      console.log(`Refer: ${jung_gid} ${jung_code} N 1 0 0 1 0 0 2`);
      console.log(`Refer: ${jong_gid} ${jong_code} N 1 0 0 1 0 0 2`);
      console.log(`EndChar`);
      console.log();
      code++;
      gid++;
    }
  }
}
console.log(`EndChars`);
console.log(`EndSplineFont`);
