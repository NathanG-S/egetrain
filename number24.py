f = open('24.txt')
s = f.readline()
for i in s:
    if i != 'K' and i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9':
        s = s.replace(i, '#')
lst = s.split('#')

num_lst = [i for i in lst if i != '' and len(i) == 15]

new = [i[2:13] for i in num_lst]

final_list = [i for i in new if i[0] == '4' and i[1] == '3' and i[4] == '7' and i[5] == '8' and i[9] == '3' and i[10] == '4']
print(max(map(int, final_list)))

#Output: 43997853334
#3*9*9*7*5*3*3*3 = 229635 - answer on task
#This script runs for about a minute because .txt file is too big.