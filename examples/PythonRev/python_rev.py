def check_password(password):
  score = 50
  try:
    if len(password) != 16:
      return 0
    if ord(password[0]) != 112: score -= 2
    if 104 != ord(password[3]): score -= 2
    if password[10] != chr(95): score -=2
    if 110 != ord(password[5]): score -= 2
    if ord(password[6]) ^ ord(password[10]) != 0: score -=2
    if password[12] != chr(115): score -=2
    if ord(password[8]) != (ord(password[7]) - ord(password[0])) + 49: score -=2
    if (ord(password[0]) - ord(password[1])) + 125 != ord(password[2]): score -= 2
    if password[14] != chr(101):score -= 2
    if ord(password[1]) - 9 != ord(password[0]): score -= 2
    if password[9] != chr(118): score -= 2
    if password[11] != chr(49): score -= 2
    if ord(password[7]) - ord(password[0]) != 2: score -= 2
    if str(0) != password[4]: score -= 2
    if ord(password[13]) != ord(password[6]) or password[15] != 'Z'.lower(): score -= 2
  except Exception:
    score = 0

  return score