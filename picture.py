from tkinter import *


def main():
    root = Tk()
    p = Picture(root)
    p.pack()
    p.draw_picture()
    root.mainloop()


class Picture(Canvas):
    def draw_picture(self):
        self.configure(width=400, height=400, bg="white")
        self.draw_sun()
        self.draw_house()
        self.draw_grass()
        print(self.winfo_x())

    def draw_sun(self):
        x, y = 350, 50
        r = 40
        self.create_oval((x-r, y-r), (x+r, y+r), fill="orange", width=0)

    def draw_house(self):
        x, y = 200, 300
        w = 100
        bw = w * 3 // 5
        self.create_rectangle((x-bw, y-bw), (x+bw, y+bw),
                              fill="lightblue", width=0)
        self.create_polygon((x-w, y-bw), (x+w, y-bw), (x, y-3*w//2),
                            fill="lightblue", width=0)

    def draw_grass(self):
        y = 400
        r = 50
        for x in range(0, 500, 10):
            self.create_arc((x-r, y-r), (x+r), (y+r), start=200, extent=-70,
                            width=3, outline="green", style=ARC)


main()
