
matrix = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 20, 12, 1],
    [43, 1, 4, -2, 1, 55],
    [3, 4, 32, 1, 10, -7],
    [2, 5, 2, 1, 41, 1],
    [1, 2, 4, 5, 9, 19]
]
# Движение по столбцам
# for i in range(6):
#    for j in range(6):
#        print(matrix[j][i])

# Максимум в последнем столбце
last_max_lst = [matrix[i][5] for i in range(6)]
last_max_num = max(last_max_lst)

# Индексы макисмума
for i in range(6):
    for j in range(6):
        if matrix[i][j] == last_max_num:
            max_row = i
            max_col = j

print(matrix[max_row])  # Строка проходящая через максимум
print([matrix[i][max_col] for i in range(6)])  # Столбец


matrix = [
    [1, 2, 3, 4, 5, 6, 78, 2],
    [7, 8, 9, 20, 12, 1, 71, 1],
    [43, 1, 4, -2, 1, 55, 32, 7],
    [3, 4, 32, 1, 10, -7, 2, 1],
    [2, 5, 2, 1, 41, 1, 90, -25],
    [1, 2, 4, 5, 9, 19, 77, 15]
]

a = []
for i in range(6):
    for j in range(8):
        a.append(matrix[i][j])

circle_lst = []
second_max = sorted(a)[-2]
print(second_max)
for i in range(6):
    for j in range(8):
        if matrix[i][j] == second_max:
            max_row = i
            max_col = j

print(max_row, max_col)

if max_row != 0:
    circle_lst.append(matrix[max_row - 1][max_col])
if max_row != 5:
    circle_lst.append(matrix[max_row + 1][max_col])
if max_col != 0:
    circle_lst.append(matrix[max_row][max_col - 1])
if max_col != 7:
    circle_lst.append(matrix[max_row][max_col + 1])
if max_row != 0 and max_col != 0:
    circle_lst.append(matrix[max_row - 1][max_col - 1])
if max_row != 5 and max_col != 7:
    circle_lst.append(matrix[max_row + 1][max_col + 1])
if max_row != 0 and max_col != 7:
    circle_lst.append(matrix[max_row - 1][max_col + 1])
if max_row != 5 and max_col != 0 :
    circle_lst.append(matrix[max_row + 1][max_col - 1])
print(circle_lst)

# 0 1 2 1 0
# a = [0, 1, 2, 3, 4]
# ||2-n| -2|
#

from random import *

a = [0, 1, 2, 3, 4, 5, 6]
for i in a:
    print(abs(abs(3 - i) - 3))

matrix = [[randint(-10, 10) for i in range(5)] for j in range(5)]
a = []
for i in range(len(matrix[0])):
    a.append(abs(abs(2 - i) - 2))
for i in matrix:
    print(i)
print('\n')
new = [[i[j] for i in matrix] for j in range(5)]
for i in new:
    print(i)
print('\n')
s = 0
new_lst = []
for j in new:
    j = j[:a[s]] + sorted(j[a[s]: len(j) - a[s]])[::-1] + j[len(j) - a[s]:]
    new_lst.append(j)
    s += 1
print('\n')
for i in new_lst:
    print(i)
print('\n')
final = [[i[j] for i in new_lst] for j in range(5)]
for i in final:
    print(i)


a = [8, 7, 10, 3, 5, 4]
# Сортировка пузырьком
for i in range(1, len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

# Сортировка выбором
for i in range(len(a) - 1):
    minimal = i
    for j in range(i + 1, len(a)):
        if a[j] < a[minimal]:
            minimal = j
    a[i], a[minimal] = a[minimal], a[i]
print(a)
