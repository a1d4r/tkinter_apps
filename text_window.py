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
        self.button = Button(self.menu, text="Изменить")
        self.entry_height = Entry(self.menu, width=3)
        self.entry_width = Entry(self.menu, width=3)
        self.menu.pack(side=TOP)
        self.button.pack(side=RIGHT)
        self.entry_height.pack(side=TOP)
        self.entry_width.pack(side=BOTTOM)

    def init_text(self, master):
        self.text = Text(master, height=10, width=20)
        self.text.pack(side=TOP)



main()
