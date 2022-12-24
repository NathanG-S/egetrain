num = []
for x in range(10):
    for z in range(10):
        for y in range(10):
            s = f'12{x}{z}4{y}65'
            if int(s) % 161 == 0 and int(s) <= 10 ** 8:
                num.append(int(s))


for i in range(124065, 12994966):

    if i % 161 == 0 and len(str(i)) >= 7 and str(i)[0] == '1' and str(i)[1] == '2' and str(i)[6] == '5' and str(i)[5] == '6' and str(i)[3] == '4':
        num.append(int(i))
        break

print(sorted(num))
new = [i/161 for i in sorted(num)]
print(new)

"""
1234065 7665
12004965 74565
12214265 75865
12294765 76365
12504065 77665
12584565 78165
12874365 79965
12954865 80465
"""
