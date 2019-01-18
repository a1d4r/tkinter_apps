from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def main():
    root = Tk()
    m = MainWindow(root)
    root.mainloop()


class MainWindow:
    def __init__(self, master):
        self.init_menu(master)
        self.init_text_section(master)
        master.bind("<Control-o>", lambda event: self.open_file())
        master.bind("<Control-s>", lambda event: self.save_file())
        master.bind("<Control-q>", lambda event: master.destroy())

    def init_menu(self, master):
        self.menu = Frame(master)
        self.menu.pack(side=TOP, ipady=4)
        self.init_buttons()
        self.configure_buttons()

    def init_text_section(self, master):
        self.text_section = Frame(master)
        self.text_section.pack(side=BOTTOM)
        self.init_scrollbars()
        self.init_text()
        self.configure_text()
        self.configure_scrollbars()

    def init_buttons(self):
        self.open_button = Button(self.menu, text="Открыть", width=8)
        self.save_button = Button(self.menu, text="Сохранить", command=self.save_file, width=8)
        self.open_button.pack(side=LEFT, padx=4)
        self.save_button.pack(side=LEFT, padx=4)

    def configure_buttons(self):
        self.open_button.config(command=self.open_file)
        self.save_button.config(command=self.save_file)

    def init_text(self):
        self.text = Text(self.text_section, height=20, width=40)
        self.text.pack(side=TOP, fill=BOTH, expand=TRUE)

    def configure_text(self):
        self.text.config(xscrollcommand=self.horizonal_scrollbar.set)
        self.text.config(yscrollcommand=self.vertical_scrollbar.set)
        self.text.config(wrap=NONE)

    def init_scrollbars(self):
        self.horizonal_scrollbar = Scrollbar(self.text_section, orient=HORIZONTAL)
        self.horizonal_scrollbar.pack(side=BOTTOM, fill=X, expand=FALSE)
        self.vertical_scrollbar = Scrollbar(self.text_section, orient=VERTICAL)
        self.vertical_scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)

    def configure_scrollbars(self):
        self.horizonal_scrollbar.config(command=self.text.xview)
        self.vertical_scrollbar.config(command=self.text.yview)

    def open_file(self):
        print("open")
        filename = fd.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*")])
        try:
            f = open(filename, "r")
            self.text.delete("1.0", END)
            self.text.insert("1.0", ''.join(f.readlines()))
        except:
            mb.showerror(title="Ошибка", message="Не удалось открыть файл")


    def save_file(self):
        filename = fd.asksaveasfilename(filetypes=[("Text files", "*.txt"), ("All files", "*")])
        try:
            f = open(filename, "w")
            text = self.text.get("1.0", END)
            f.write(text[:-1])
        except:
            mb.showerror(title="Ошибка", message="Не удалось сохранить файл")


main()
