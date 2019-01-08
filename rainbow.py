from tkinter import *
from functools import partial


class Rainbow:
    colors = ["#ff0000", "#ff7d00", "#ffff00", "#00ff00", "#007dff", "#0000ff", "#7d00ff"]
    names = ["красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"]

    def __init__(self, master):
        self.label = Label(master)
        self.entry = Entry(master, justify=CENTER)
        self.colors_frame = Frame(master)
        self.buttons = [Button(self.colors_frame, bg=self.colors[i], height=1, width=2,
                        command=partial(self.print_color, i)) for i in range(len(self.colors))]
        self.label.pack()
        self.entry.pack()
        self.colors_frame.pack(pady=2)
        for button in self.buttons:
            button.pack(side="left", padx=1, pady=1)

    def print_color(self, i):
        self.label["text"] = self.names[i]
        self.entry.delete(0, END)
        self.entry.insert(0, self.colors[i])


root = Tk()

rainbow = Rainbow(root)
root.mainloop()
