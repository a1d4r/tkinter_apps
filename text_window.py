from tkinter import *


def main():
    root = Tk()
    m = MainWindow(root)
    root.mainloop()


class MainWindow:
    def __init__(self, master):
        self.init_menu(master)
        self.init_text(master)

    def init_menu(self, master):
        self.menu = Frame(master)
        self.button = Button(self.menu, text="Изменить", command=lambda: self.resize(None))
        self.entry_height = Entry(self.menu, width=3)
        self.entry_width = Entry(self.menu, width=3)
        self.menu.pack(side=TOP)
        self.button.pack(side=RIGHT)
        self.entry_height.pack(side=TOP)
        self.entry_width.pack(side=BOTTOM)

        self.button.bind("<Return>", self.resize)
        self.entry_height.bind("<Return>", self.resize)
        self.entry_width.bind("<Return>", self.resize)

    def resize(self, event):
        new_height = int(self.entry_height.get())
        new_width = int(self.entry_width.get())
        self.text.configure(height=new_height, width=new_width)

    def init_text(self, master):
        self.text = Text(master, height=10, width=20)
        self.text.pack(side=TOP)

        self.text.bind('<FocusIn>', self.paint_in_white)
        self.text.bind('<FocusOut>', self.paint_in_gray)

    def paint_in_gray(self, event):
        self.text["bg"] = "lightgray"

    def paint_in_white(self, event):
        self.text["bg"] = "white"



main()
