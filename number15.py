for a in range(1, 2000):
    ok = True
    for x in range(1, 2000):
        if not (((x % 175 == 0) <= (x % 25 != 0)) or (2 * x + a >= 1780)):
            ok = False
            break
    if ok:
        print(a)
        break