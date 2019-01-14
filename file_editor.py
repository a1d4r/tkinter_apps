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
        self.menu = Frame(master)
        self.menu.pack(side=TOP)
        self.init_entry()
        self.init_buttons()

    def init_text_section(self, master):
        self.middle_frame = Frame(master)
        self.bottom_frame = Frame(master)
        self.middle_frame.pack(side=TOP)
        self.bottom_frame.pack(side=TOP)
        self.init_text()
        self.init_scrollbars()

    def init_entry(self):
        self.entry = Entry(self.menu)
        self.entry.pack(side=LEFT)

    def init_buttons(self):
        self.open_button = Button(self.menu, text="Открыть")
        self.save_button = Button(self.menu, text="Сохранить")
        self.open_button.pack(side=RIGHT)
        self.save_button.pack(side=RIGHT)

    def init_text(self):
        self.text = Text(self.middle_frame)
        self.text.pack(side=LEFT)

    def init_scrollbars(self):
        self.vertical_scrollbar = Scrollbar(self.middle_frame, orient=VERTICAL)
        self.vertical_scrollbar.pack(side=RIGHT)
        self.horizonal_scrollbar = Scrollbar(self.bottom_frame, orient=HORIZONTAL)
        self.horizonal_scrollbar.pack()


main()