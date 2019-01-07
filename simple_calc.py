# Простейший калькулятор
from tkinter import *


class Calculator:
    def __init__(self, master):
        self.entry_1 = Entry(master, width=20)
        self.entry_2 = Entry(master, width=20)
        self.label_answer = Label(master)
        self.button_sum = Button(master, text="+")
        self.button_difference = Button(master, text="-")
        self.button_product = Button(master, text="*")
        self.button_quotient = Button(master, text="/")

        self.entry_1.pack()
        self.entry_2.pack()
        self.button_sum.pack()
        self.button_difference.pack()
        self.button_product.pack()
        self.button_quotient.pack()


root = Tk()

calc = Calculator(root)

root.mainloop()