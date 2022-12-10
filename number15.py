#15 номер
for a in range(1, 2000):
    ok = True
    for x in range(1, 2000):
        if not (((x % 175 == 0) <= (x % 25 != 0)) or (2 * x + a >= 1780)):
            ok = False
            break
    if ok:
        print(a)
        break
        
# 5722 поляков номер 5
cnt = 0
for N in range(1000, 10001):
    R = str(int(N))
    if int(R[0]) % 4 == 0:
        R = '9' + R[1:]
    elif int(R[0]) % 2 == 0 and int(R[0]) % 4 != 0:
        R = '3' + R[1:]
    if R[0] == '9' and oct(int(R))[-1] == '4':
        cnt += 1
print(cnt)

# 5720 поляков номер 8
from itertools import product

words = product('POLYGON', repeat=5)
set_words = []
for word in words:
    new_word = ''.join(word)
    if new_word == new_word[::-1] and (new_word[2] == 'O' or new_word[2] == 'Y'):
        set_words.append(new_word)

print(len(set(set_words)))

# 5727 поляков
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

#5605 номер 16
from sys import setrecursionlimit

setrecursionlimit(10_000)


def f(n):
    if round(n ** 0.5) == n ** 0.5:
        return n ** 0.5
    else:
        return f(n + 1) + 1


print(f(4850) + f(5000))
