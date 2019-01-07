from tkinter import *

# Создать главное окно.
root = Tk()

# Создать виджеты и выполнить конфигурацию их свойств
e = Entry(root, width=20)
b = Button(root, text="Преобразовать")
l = Label(root, bg="Black", fg="white", width=20)

# Определить обработчики событий
def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l["text"] = ' '.join(s)

# Определить события
b.bind('<Button>', strToSortlist)

# Расположить виджеты в главном окне
e.pack()
b.pack()
l.pack()

# Запустить цикл обработки событий
root.mainloop()
