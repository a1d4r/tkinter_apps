from tkinter import *
from functools import partial


class Rainbow:
    colors = ["#ff0000", "#ff7d00", "#ffff00", "#00ff00", "#007dff", "#0000ff", "#7d00ff"]
    names = ["красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"]

    def __init__(self, master):
        self.label = Label(master)
        self.entry = Entry(master, justify=CENTER)
        self.buttons = [Button(bg=self.colors[i], command=partial(self.print_color, i), width=15)
                   for i in range(len(self.colors))]
        self.label.pack()
        self.entry.pack()
        for button in self.buttons:
            button.pack()

    def print_color(self, i):
        self.label["text"] = self.names[i]
        self.entry.delete(0, END)
        self.entry.insert(0, self.colors[i])


root = Tk()

rainbow = Rainbow(root)
root.mainloop()
