def is_challenge2_password(password: str) -> bool:
    score = 150

    if len(password) != 26:
        score = 0
        return

    if not password.islower() or not password.isalpha():
        score = 0
        return

    values = [149, 156, 157, 158, 159, 162, 163, 165, 167, 170, 172]
    if any((chr(v - 50)) in password for v in values):
        score -= 30

    if password[::2][5::-1][0] != "t":
        score -= 3

    if password[::2][5::-1][1] != "g":
        score -= 3

    if password[::2][5::-1][2] != "o":
        score -= 3

    if password[::2][5::-1][3] != "r":
        score -= 3

    if password[::2][5::-1][4] != "v":
        score -= 3

    if password[::2][5::-1][5] != "n":
        score -= 3

    if password[5] == password[22]:
        score -= 1

    if password[4] != password[24]:
        score -= 1

    if password[:7].count('e') != 2:
        score -= 1

    try:
        if int(''.join([str(password[-5::].find(c)) for c in "gabed"])) != -12014:
            score -= 20
    except:
        score -= 20

    if password[12] != password[23]:
        score -= 1

    if password[11:15].count('d') != 3:
        score -= 2

    if password[16:21] != "white":
        score -= 30

    if password[4:8:3] != password[7:3:-3]:
        score -= 2

    if "freddy" not in password[1::2]:
        score -= 3

    return score
