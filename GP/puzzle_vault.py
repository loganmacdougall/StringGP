def check_password(parameter):
  score = 50
  try:
    if (len(parameter) != 0x19):
      score -= 10
    
    if (parameter[0x0] != "T"):
      score -= 1

    if parameter[2] != parameter[4]:
      score -= 2
    
    if parameter[10] != parameter[21]:
      score -= 2
    
    if parameter[11] != parameter[22]:
      score -= 2
    
    if parameter[12] != parameter[23]:
      score -= 2
    
    if parameter[13] != parameter[24]:
      score -= 2
    
    if parameter[6] != parameter[19]:
      score -= 2

    if parameter[0x2] != chr(0x65):
      score -= 1

    if ord(parameter[0x6]) != 0x73:
      score -= 1
    
    if ord(parameter[0x7]) * 0x100 + ord(parameter[0x3]) != 0x4e72:
      score -= 2

    if (ord(parameter[0x5]) * 0x539 + 0x7a69 != 0x1f7aa):
      score -= 1

    val = ord(parameter[0x9])
    if chr(((val << 0x3) | (val >> 0x5)) & 0xff) != "2":
      score -= 2

    if parameter[0x15:0x19][::-1] != "tlua":
        score -= 4

    nopass = "No,\x20this\x20is\x20not\x20the\x20password"
  
    if nopass[len(nopass) - 0x17] != parameter[0x1]:
      score -= 1

    if (nopass[0x19] != parameter[0x8]):
      score -= 2

    _0x1a21fd = [0x20, 0x1d, 0x74, 0x6, 0x6, 0x7, 0x76]
    for i in range(len(_0x1a21fd)):
      if chr(_0x1a21fd[i] ^ ord(nopass[0x9 + i])) != parameter[0xe + i]:
            score -= 1
  except Exception:
    score = 0

  return score