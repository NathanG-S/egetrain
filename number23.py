# 5543 Поляков
# (М.Шагитов)
def f(x, y):
    if x > y or x == 3:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 2, y) + f(x * 3, y) + f(x * 4, y)


print(f(1, 600))


# 5544 Поляков
# (М.Шагитов)
def f(start, end, tr=None):
    if tr is None:
        tr = []
    tr = tr + [start]
    if start == end:
        for i in range(len(tr)):
            if sum(tr[i:i + 3]) % 11 == 0:
                return 1
        return 0
    elif start > end:
        return 0
    else:
        return f(start + 2, end, tr) + \
            f(start * 3, end, tr) + \
            f(start * 4, end, tr)


print(f(1, 600))


# 5274 Поляков
# (М.Шагитов)
def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 1, y) + (f(10 * x + 1, y) if (10 * x + 1) % 3 == 0 else 0) + f(x * 5, y)


print(f(1, 410))
