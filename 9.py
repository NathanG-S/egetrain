f = open('9.txt')
count = 0
for i in f:
    s = [int(x) for x in i.split()]
    double = sum(s) - sum(set(s))
    if (len(set(s)) != len(s)) and ((sum(s) - 2*double) % 2 != 0):
        count += 1

print(count)

