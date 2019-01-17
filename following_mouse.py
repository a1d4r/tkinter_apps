from tkinter import *


class MyCanvas(Canvas):
    ball_speed = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(width=600, height=600, bg="white")
        self.ball = self.create_oval((100, 100), (150, 150), width=0, fill="red")
        self.bind('<Button-1>', self.move_to_cursor)

    def move_to_cursor(self, event):
        c = self.coords(self.ball)
        x, y = (c[0] + c[2]) / 2, (c[1] + c[3]) / 2
        dx = event.x - x
        dy = event.y - y
        dist = (dx**2 + dy**2) ** 0.5
        speed_x = self.ball_speed * dx / dist
        speed_y = self.ball_speed * dy / dist

        self.move(self.ball, speed_x, speed_y)

        if abs(dx) > 2 * self.ball_speed or abs(dy) > 2 * self.ball_speed:
            root.after(5, lambda: self.move_to_cursor(event))


root = Tk()
c = MyCanvas(root)
c.pack()
root.mainloop()