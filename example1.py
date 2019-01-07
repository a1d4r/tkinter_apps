from tkinter import *

class Block:
    def __init__(self, master):
        """
        Инициализация виджетов в главном окне
        :param master: главное окно, в котором будут располагаться виджеты
        """
        self.e = Entry(master, width=20)
        self.b = Button(master, text="Преобразовать")
        self.l = Label(master, bg="Black", fg="white", width=20)
        self.b.bind('<Button>', self.strToSortlist)
        self.e.pack()
        self.b.pack()
        self.l.pack()
    def strToSortlist(self, event):
        """
        Сортирует слова в поля ввода и выводит их в нижнее окно
        """
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l["text"] = ' '.join(s)

# Создать главное окно.
root = Tk()

block = Block(root)

# Запустить цикл обработки событий
root.mainloop()
