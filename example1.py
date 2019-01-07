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
        self.e.pack()
        self.b.pack()
        self.l.pack()
    def setFunc(self, func):
        self.b['command'] = eval('self.' + func)
    def wordsSort(self):
        """ Сортирует слова, записанные в поле ввода """
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l["text"] = ' '.join(s)
    def wordsReverse(self):
        """ Меняет порядок слов, записанных в поле ввода, на противоположный """
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l['text'] = ' '.join(s)

# Создать главное окно.
root = Tk()

block_1 = Block(root)
block_1.setFunc('wordsSort')

block_2 = Block(root)
block_2.setFunc('wordsReverse')

# Запустить цикл обработки событий
root.mainloop()
