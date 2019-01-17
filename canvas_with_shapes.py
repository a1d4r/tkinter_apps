from tkinter import *


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Прямовал")
        self.init_canvas()
        self.init_button()

    def init_canvas(self):
        self.canvas = Canvas(self, bg="White", height=400, width=400)
        self.canvas.pack(side=TOP)

    def init_button(self):
        self.button = Button(self, text="Добавить фигуру",
                             command=self.create_figure_window)
        self.button.pack(side=TOP)

    def create_figure_window(self):
        w = FigureWindow(self)


class FigureWindow(Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Фигура")


root = MainWindow()

root.mainloop()