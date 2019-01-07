# Простейший калькулятор
from tkinter import *


class Calculator:
    def __init__(self, master):
        self.entry1 = Entry(master, width=20)
        self.entry2 = Entry(master, width=20)
        self.label_answer = Label(master)
        self.button_sum = Button(master, text="+")
        self.button_difference = Button(master, text="-")
        self.button_product = Button(master, text="*")
        self.button_quotient = Button(master, text="/")

        self.entry1.pack()
        self.entry2.pack()
        self.button_sum.pack()
        self.button_difference.pack()
        self.button_product.pack()
        self.button_quotient.pack()
        self.label_answer.pack()

        self.button_sum["command"] = self.calc_sum
        self.button_difference["command"] = self.calc_difference
        self.button_product["command"] = self.calc_product
        self.button_quotient["command"] = self.calc_quotient

    def valid_input(self):
        """ Корректны ли данные в полях ввода? """
        return self.entry1.get().isnumeric() and self.entry2.get().isnumeric()

    def numbers(self):
        """ Кортеж из двух чисех в полях ввода """
        return int(self.entry1.get()), int(self.entry2.get())

    def sum(self):
        number1, number2 = self.numbers()
        return number1 + number2

    def difference(self):
        number1, number2 = self.numbers()
        return number1 - number2

    def product(self):
        number1, number2 = self.numbers()
        return number1 * number2

    def quotient(self):
        number1, number2 = self.numbers()
        return number1 / number2

    def calc_sum(self):
        if self.valid_input():
            self.label_answer["text"] = str(self.sum())
        else:
            self.label_answer["text"] = "Ошибка"

    def calc_difference(self):
        if self.valid_input():
            self.label_answer["text"] = str(self.difference())
        else:
            self.label_answer["text"] = "Ошибка"

    def calc_product(self):
        if self.valid_input():
            self.label_answer["text"] = str(self.product())
        else:
            self.label_answer["text"] = "Ошибка"

    def calc_quotient(self):
        if self.valid_input() and self.numbers()[1] != 0:
            self.label_answer["text"] = str(self.quotient())
        else:
            self.label_answer["text"] = "Ошибка"


root = Tk()

calc = Calculator(root)

root.mainloop()