from tkinter import *
from tkinter import ttk

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
        self.menu.pack(side=TOP, ipady=4)
        self.init_entry()
        self.init_buttons()

    def init_text_section(self, master):
        self.text_section = Frame(master)
        self.text_section.pack(side=BOTTOM)
        self.init_scrollbars()
        self.init_text()

    def init_entry(self):
        self.entry = Entry(self.menu, width=20)
        self.entry.pack(side=LEFT, padx=6)

    def init_buttons(self):
        self.open_button = Button(self.menu, text="Открыть", width=10)
        self.save_button = Button(self.menu, text="Сохранить", width=10)
        self.save_button.pack(side=LEFT, padx=4)
        self.open_button.pack(side=LEFT, padx=4)

    def init_text(self):
        self.text = Text(self.text_section, height=20, width=40)
        self.text.pack(side=TOP, fill=BOTH, expand=TRUE)

    def init_scrollbars(self):
        self.horizonal_scrollbar = Scrollbar(self.text_section, orient=HORIZONTAL)
        self.horizonal_scrollbar.pack(side=BOTTOM, fill=X, expand=FALSE)
        self.vertical_scrollbar = Scrollbar(self.text_section, orient=VERTICAL)
        self.vertical_scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)

main()