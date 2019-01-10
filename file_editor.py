from tkinter import *


def main():
    root = Tk()
    m = MainWindow(root)
    root.mainloop()


class MainWindow:
    def __init__(self, master):
        self.init_menu(master)
        self.init_text_section(master)

    def init_menu(self, master):
        self.menu = Frame()
        self.init_entry()
        self.init_buttons()

    def init_text_section(self, master):
        self.text_section = Frame()
        self.init_text()
        self.init_scrollbars()

    def init_entry(self):
        pass

    def init_buttons(self):
        pass

    def init_text(self):
        pass

    def init_scrollbars(self):
        pass

main()