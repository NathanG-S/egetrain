'''f = open('24.txt')
s = f.readline()
for i in s:
    if i != 'K' and i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9':
        s = s.replace(i, '#')
lst = s.split('#')

num_lst = [i for i in lst if i != '' and len(i) == 15]

new = [i[2:13] for i in num_lst]

final_list = [i for i in new if
              i[0] == '4' and i[1] == '3' and i[4] == '7' and i[5] == '8' and i[9] == '3' and i[10] == '4']
print(max(map(int, final_list)))

# Output: 43997853334
# 3*9*9*7*5*3*3*3 = 229635 - answer on task
# This script runs for about a minute because .txt file is too big.

# 5392 Поляков
# #-буква $-цифра   #$Z#
# буква цифра буква = #$#
# #$#$##$##$##$##$##

f = open('24_2.txt')
s = f.readline()
for i in s:
    if i == 'A' or i == 'B' or i == 'C':
        s = s.replace(i, '#')
    if i == '1' or i == '2' or i == '3':
        s = s.replace(i, '$')

s = s.replace("$##", 'Z')

counts = []
cts = 0
for i in range(len(s)):
    if s[i] == 'Z':
        cts += 1
    if s[i] == 'Z' and s[i + 1] != 'Z':
        counts.append(cts)
        cts = 0

print(sorted(counts)[-1])
'''
f = open('24-3.txt')
s = f.readline().strip()
s = s.split('.')
#b = [j for j in s if j != '']
m = len(s)

for x in range(len(s)-7):
    c = '.' + s[x] + '.' + s[x+1] + '.' +s[x+2] + '.' + s[x+3] + '.' + s[x+4] + '.' + s[x+5] + '.'
    m = min(m, len(c))

print(m)


'''m = len(s) + 1
for i in range(len(s)-6):
    c = '.' + '.'.join(s[i:i+6]) + '.'
    m = min(m, len(c))

print(m)'''