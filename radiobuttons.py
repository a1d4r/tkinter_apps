from tkinter import *


def main():
    root = Tk()
    m = MainWindow(root)
    root.mainloop()


class MainWindow:
    button_values = ['Вася', 'Петя', 'Витя']
    label_values = ['+7 900-555-33-44', '+7 960-444-22-11', '+7 940-777-55-88']

    def __init__(self, master):
        self.buttons = Frame(master)
        self.label = Label(master)
        self.buttons.pack(side=LEFT)
        self.label.pack(side=LEFT)
        self.init_buttons()

    def init_buttons(self):
        self.value = IntVar()
        self.value.set(0)
        self.update_label()
        self.rbutton1 = Radiobutton(self.buttons, variable=self.value, value=0, text=self.button_values[0],
                                    indicatoron=0, command=self.update_label)
        self.rbutton2 = Radiobutton(self.buttons, variable=self.value, value=1, text=self.button_values[1],
                                    indicatoron=0, command=self.update_label)
        self.rbutton3 = Radiobutton(self.buttons, variable=self.value, value=2, text=self.button_values[2],
                                    indicatoron=0, command=self.update_label)
        self.rbutton1.pack(side=TOP)
        self.rbutton2.pack(side=TOP)
        self.rbutton3.pack(side=TOP)

    def update_label(self):
        self.label["text"] = self.label_values[self.value.get()]


main()