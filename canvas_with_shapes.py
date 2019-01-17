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
                             command=self.create_figure_window, width=20)
        self.button.pack(side=TOP, pady=4)

    def create_figure_window(self):
        w = FigureWindow(self.draw_rectangular, self.draw_oval)

    def draw_rectangular(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2)

    def draw_oval(self, x1, y1, x2, y2):
        self.canvas.create_oval(x1, y1, x2, y2)


class FigureWindow(Toplevel):
    def __init__(self, draw_rectangular, draw_oval, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Фигура")
        self.init_first_point_frame()
        self.init_second_point_frame()
        self.init_radiobuttons()
        self.init_button(draw_rectangular, draw_oval)

    def init_first_point_frame(self):
        self.frame1 = LabelFrame(self, text="Координаты первой точки")
        self.entry_x1 = Entry(self.frame1, width=10)
        self.entry_y1 = Entry(self.frame1, width=10)

        self.frame1.pack(side=TOP)
        self.entry_x1.pack(side=LEFT, padx=10)
        self.entry_y1.pack(side=LEFT, padx=10)

    def init_second_point_frame(self):
        self.frame2 = LabelFrame(self, text="Координаты второй точки")
        self.entry_x2 = Entry(self.frame2, width=10)
        self.entry_y2 = Entry(self.frame2, width=10)

        self.frame2.pack(side=TOP)
        self.entry_x2.pack(side=LEFT, padx=10)
        self.entry_y2.pack(side=LEFT, padx=10)

    def init_radiobuttons(self):
        self.frame3 = LabelFrame(self, text="Выберите фигуру")
        self.value = IntVar()
        self.value.set(0)
        self.button_rectangle = Radiobutton(self.frame3, value=0, variable=self.value,
                                            text="Прямоугольник")
        self.button_oval = Radiobutton(self.frame3, value=1, variable=self.value,
                                       text="Овал")
        self.frame3.pack(side=TOP)
        self.button_rectangle.pack(side=TOP, anchor="w")
        self.button_oval.pack(side=TOP, anchor="w")

    def init_button(self, draw_rectangular, draw_oval):
        self.button_draw = Button(self, text="Нарисовать", width=20)
        self.button_draw["command"] = lambda: self.draw_figure(draw_rectangular, draw_oval)
        self.button_draw.pack(side=TOP, pady=6)

    def draw_figure(self, draw_rectangular, draw_oval):
        x1 = int(self.entry_x1.get())
        y1 = int(self.entry_y1.get())
        x2 = int(self.entry_x2.get())
        y2 = int(self.entry_y2.get())
        if self.value.get() == 0:
            draw_rectangular(x1, y1, x2, y2)
        else:
            draw_oval(x1, y1, x2, y2)
        self.destroy()


root = MainWindow()

root.mainloop()