# 2801 поляков
for n in range(1,100):
    for b in range(1,100):
        for a in range(1,100):
            if (-1 + n*(a-1) - 24 == 0) and (2 + n*(b-2) - 12 == 0):
                print(n)

# 2799 поляков. тут b принимает отрицательное значение при решении руками поэтому если код не срабатывает задай
# диапазон с учетом отрицательных чисел Также можно понять исходя из выражения в условии что значения будут
# отрицательными
for n in range(-100, 100):
    for b in range(-100, 100):
        for a in range(-100, 100):
            if (-7 + n * (15 + a) + 23 == 1) and (-1 + n * (22 + b) - 32 == -3):
                print(n)

# 2798  поляков
for a in range(-100,100):
    for b in range(-100,100):
        if (1 + 3*(a+4) + 17 == 0) and (-1 + 3*(b+5) +31 == 0):
            print(a,b)

# 2793 поляков
for n in range(1,200):
    for a in range(1,200):
        for b in range(1,200):
            if (1 + n*(a-1) -25 == 0) and (-3 + n*(b-2) -33 == 0):
                print(n)

# 2791 поляков
for a in range(1,200):
    for b in range(1,200):
        for c in range(1,200):
            if (4 + 4*(2 + a) == 24) and (8 + 4*(-4+b) == 16) and (12 + 4*(-5 + c) == 12):
                print(a,b,c)
#5727 поляков
for n in range(20,100):
    s = '3'*n + '2'*n + '1'*n
    while '21' in s or '31' in s or '32' in s:
        if '21' in s:
            s = s.replace('21', '12', 1)
        elif '31' in s:
            s = s.replace('31', '13', 1)
        elif '32' in s:
            s = s.replace('32', '23', 1)
    if s[49] == '2':
        print(len(s))
        break