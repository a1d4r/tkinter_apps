from tkinter import *


def main():
    root = Tk()
    p = Picture(root)
    p.pack()
    p.draw_picture()
    root.mainloop()


class Picture(Canvas):
    def draw_picture(self):
        self.draw_sun()
        self.draw_house()
        self.draw_grass()

    def draw_sun(self):
        pass

    def draw_house(self):
        pass

    def draw_grass(self):
        pass


main()
