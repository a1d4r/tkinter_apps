from tkinter import *


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Прямовал")
        self.init_canvas()
        self.init_button()
        self.centralize_window()

    def centralize_window(self):
        self.update_idletasks()
        screen_w, screen_h = self.winfo_screenwidth(), self.winfo_screenheight()
        window_w, window_h = map(int, self.geometry().split('+')[0].split('x'))
        window_x = screen_w // 2 - window_w // 2
        window_y = screen_h // 2 - window_h // 2
        self.geometry('+{}+{}'.format(window_x, window_y))

    def init_canvas(self):
        self.canvas = Canvas(self, bg="White", height=400, width=400)
        self.canvas.pack(side=TOP)

    def init_button(self):
        self.button = Button(self, text="Добавить фигуру",
                             command=self.create_figure_window, width=20)
        self.button.pack(side=TOP, pady=4)

    def create_figure_window(self):
        w = FigureWindow(self)

    def draw_rectangular(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2)

    def draw_oval(self, x1, y1, x2, y2):
        self.canvas.create_oval(x1, y1, x2, y2)


class FigureWindow(Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Фигура")
        self.init_first_point_entries()
        self.init_second_point_entries()
        self.init_radiobuttons()
        self.init_button(master.draw_rectangular, master.draw_oval)
        self.align_window(master)

    def align_window(self, master):
        self.update_idletasks()
        master_w, master_h = map(int, master.geometry().split('+')[0].split('x'))
        master_x, master_y = map(int, master.geometry().split('+')[1:])
        window_w, window_h = map(int, self.geometry().split('+')[0].split('x'))
        window_x = master_x + master_w
        window_y = master_y
        print(master_w, master_h)
        print(master_x, master_y)
        print(window_w, window_h)
        print(window_x, window_y)
        self.geometry('+{}+{}'.format(window_x, window_y))

    def init_first_point_entries(self):
        Label(self, text="x1").grid(row=0, column=0, sticky=E, pady=6)
        self.entry_x1 = Entry(self, width=4)
        self.entry_x1.grid(row=0, column=1, sticky=W)
        Label(self, text="y1").grid(row=0, column=2, sticky=E)
        self.entry_y1 = Entry(self, width=4)
        self.entry_y1.grid(row=0, column=3, sticky=W)

    def init_second_point_entries(self):
        Label(self, text="x2").grid(row=1, column=0, sticky=E, pady=10)
        self.entry_x2 = Entry(self, width=4)
        self.entry_x2.grid(row=1, column=1, sticky=W)
        Label(self, text="y2").grid(row=1, column=2, sticky=E)
        self.entry_y2 = Entry(self, width=4)
        self.entry_y2.grid(row=1, column=3, sticky=W)

    def init_radiobuttons(self):
        self.value = IntVar()
        self.value.set(0)
        self.button_rectangle = Radiobutton(self, value=0, variable=self.value,
                                            text="Прямоугольник").grid(row=2, column=0,
                                                                       columnspan=4, sticky=W, padx=10)
        self.button_oval = Radiobutton(self, value=1, variable=self.value,
                                       text="Овал").grid(row=3, column=0,
                                                         columnspan=4, sticky=W, padx=10)

    def init_button(self, draw_rectangular, draw_oval):
        Button(self, text="Нарисовать",
               command=lambda: self.draw_figure(draw_rectangular, draw_oval)).grid(
               row=4, column=0, columnspan=4, pady=6, padx=10, sticky=W+E)

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
