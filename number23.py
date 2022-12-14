# 5543 Поляков
def f(x, y):
    if x > y or x == 3:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 2, y) + f(x * 3, y) + f(x * 4, y)


print(f(1, 600))
