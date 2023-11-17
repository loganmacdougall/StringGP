#!/usr/local/bin/node

score = 50

r1 = function (parameter) {
  try {

    if (parameter["length"] != 0x19) {
      score -= 10
    }
    if (parameter[0x0] != "T") {
      score -= 1
    }
    if (
      parameter[2] != parameter[4]
    ) {
      score -= 2
    }
    if (
      parameter[10] != parameter[21]
    ) {
      score -= 2
    }
    if (
      parameter[11] != parameter[22]
    ) {
      score -= 2
    }
    if (
      parameter[12] != parameter[23]
    ) {
      score -= 2
    }
    if (
      parameter[13] != parameter[24]
    ) {
      score -= 2
    }
    if (
      parameter[6] != parameter[19]
    ) {
      score -= 2
    }
    if (
      parameter[0x2] != String["fromCharCode"](0x65)
    ) {
      score -= 1
    }
    if (parameter["charCodeAt"](0x6) != 0x73) {
      score -= 1
    }
    if (
      parameter["charCodeAt"](0x7) * 0x100 + parameter["charCodeAt"](0x3) !=
      0x4e72
    ) {
      score -= 2
    }
    if (parameter["charCodeAt"](0x5) * 0x539 + 0x7a69 != 0x1f7aa) {
      score -= 1
    }
    //
    val = parameter["charCodeAt"](0x9);
    if (String["fromCharCode"](((val << 0x3) | (val >> 0x5)) & 0xff) != "2") {
      score -= 2
    }
    //
    if (
      parameter["substring"](0x15, 0x19)
        ["split"]("")
        ["reverse"]()
        ["join"]("") !== "tlua"
    ) {
      score -= 4
    }
    //
    nopass = "No,\x20this\x20is\x20not\x20the\x20password";
    if (
      nopass[nopass["length"] - 0x17] != parameter[0x1]
    ) {
      score -= 1
    }
    if (nopass[0x19] != parameter[0x8]) {
      score -= 2
    }
    //
    const _0x1a21fd = [0x20, 0x1d, 0x74, 0x6, 0x6, 0x7, 0x76];
    for (i = 0x0; i < _0x1a21fd["length"]; i++) {
      if (
        String["fromCharCode"](_0x1a21fd[i] ^ nopass["charCodeAt"](0x9 + i)) !=
        parameter[0xe + i]
      ) {
        score -= 1
      }
    }
  } catch {
    score = 0
  } 
};

r1(process.argv[2])

process.exit(score)