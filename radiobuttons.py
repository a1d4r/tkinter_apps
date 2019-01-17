from tkinter import *


def main():
    root = Tk()
    m = MainWindow(root)
    root.mainloop()


class MainWindow:
    def __init__(self, master):
        self.buttons = Frame(master)
        self.label = Label(master)
        self.buttons.pack(side=LEFT)
        self.label.pack(side=LEFT)
        self.rbutton1 = Radiobutton(self.buttons)
        self.rbutton2 = Radiobutton(self.buttons)
        self.rbutton3 = Radiobutton(self.buttons)
        self.rbutton1.pack(side=TOP)
        self.rbutton2.pack(side=TOP)
        self.rbutton3.pack(side=TOP)

main()