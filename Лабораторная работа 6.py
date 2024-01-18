import tkinter as tk
import math as m


def sorti(xarr):
    for i in range(len(xarr) - 1):
        for j in range(len(xarr) - i - 1):
            if xarr[j] < xarr[j + 1]:
                xarr[j], xarr[j + 1] = xarr[j + 1], xarr[j]
    ans = "Отсортированный по убыванию вектор X: "
    for i in xarr:
        ans += str("%.3f" % float(i)) + " "
    lbl9 = tk.Label(win, text=ans, wraplength=600)
    lbl9.place(x=300, y=610)
    file.write("\n")
    file.write(ans)
    file.close()


def preob(ar):
    suma = 0
    for i in range(len(ar)):
        mini = ar[0][i]
        ans = "Минимальное значение элементов " + str(i + 1) + " столбца: "
        for j in range(len(ar[i])):
            if ar[j][i] < mini:
                mini = ar[j][i]
        ans += str(mini)
        file.write("\n")
        file.write(ans)
        tk.Label(win, text=ans, wraplength=500).place(x=300, y=410 + i * 20)
    for i in range(9):
        ar[i][1], ar[i][4] = ar[i][4], ar[i][1]
    ans = "Отформатированная матрица A: "
    for i in ar:
        for j in i:
            ans += str("%.3f" % j) + ' '
        ans += "\n"
    lbl7 = tk.Label(win, text=ans, wraplength=700)
    lbl7.place(x=530, y=250)
    file.write("\n")
    file.write(ans)
    x = []
    ans = "Вектор X: "
    for i in range(9):
        w = float(ar[i][8 - i])
        x.append(w)
        ans += "%.3f" % w + " "
    lbl8 = tk.Label(win, text=ans, wraplength=500)
    lbl8.place(x=300, y=595)
    file.write("\n")
    file.write(ans)
    sorti(x)


def matrix(b):

    a = []
    ans = "Матрица A: "
    for i in range(1, 10):
        q = []
        for j in range(1, 10):
            if j + i > 4:
                w = b * i + ((((b ** j) ** 0.5) + b / j) ** 2)
                q.append(w)
                ans += str("%.3f" % w) + " "
            else:
                w = b ** 2 + i * j
                q.append(w)
                ans += str("%.3f" % w) + " "
        a.append(q)
        ans += "\n"
    lbl5 = tk.Label(win, text=ans, wraplength=500)
    lbl5.place(x=20, y=250)

    file.write("\n")
    file.write(ans)
    preob(a)


def geta():
    global file

    a = []
    b = int(vvod_b.get())
    vvod_b.delete(0, tk.END)
    file = open("output.txt", "w")
    matrix(b)


win = tk.Tk()

win.config(cursor='dot red')
win.title("Лабораторная работа 6")
win.geometry("1100x700")
win.config(bg="green")
vvod_b = tk.Entry(win, font="bold", width=10)
vvod_b.place(x=380, y=175)
task = tk.PhotoImage(file="Рисунок1.png")
lbl1 = tk.Label(win, image=task)
lbl2 = tk.Label(win, text="Введите b:")
lbl1.place(x=130, y=20)
lbl2.place(x=310, y=180)
btn1 = tk.Button(win, text='Запуск', command=geta, relief=tk.RAISED, cursor='sailboat blue blue', width=30)
btn1.config(background='lightgray')
btn1.place(x=340, y=220)
win.mainloop()
