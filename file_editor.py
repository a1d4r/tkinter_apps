from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def main():
    m = MainWindow()
    m.mainloop()


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_menu()
        self.init_text_section()
        self.init_context_menu()
        self.bind("<Control-o>", lambda event: self.open_file())
        self.bind("<Control-s>", lambda event: self.save_file())
        self.bind("<Control-q>", lambda event: self.destroy())

    def init_menu(self):
        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.menu.add_command(label="Открыть", command=self.open_file)
        self.menu.add_command(label="Сохранить", command=self.save_file)

    def init_text_section(self):
        self.init_scrollbars()
        self.init_text()
        self.configure_text()
        self.configure_scrollbars()

    def init_text(self):
        self.text = Text(self, height=20, width=40)
        self.text.pack(side=TOP, fill=BOTH, expand=TRUE)
        self.text.bind("<Button-3>", self.popup)

    def configure_text(self):
        self.text.config(xscrollcommand=self.horizonal_scrollbar.set)
        self.text.config(yscrollcommand=self.vertical_scrollbar.set)
        self.text.config(wrap=NONE)

    def init_scrollbars(self):
        self.horizonal_scrollbar = Scrollbar(self, orient=HORIZONTAL)
        self.horizonal_scrollbar.pack(side=BOTTOM, fill=X, expand=FALSE)
        self.vertical_scrollbar = Scrollbar(self, orient=VERTICAL)
        self.vertical_scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)

    def configure_scrollbars(self):
        self.horizonal_scrollbar.config(command=self.text.xview)
        self.vertical_scrollbar.config(command=self.text.yview)

    def init_context_menu(self):
        self.context_menu = Menu(tearoff=0)
        self.context_menu.add_command(label="Очистить", command=self.clear_text)

    def popup(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def open_file(self):
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

    def clear_text(self):
        self.text.delete(1.0, END)

main()
