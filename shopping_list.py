from tkinter import *


def main():
    root = Tk()
    m = MainWindow(root)
    root.mainloop()


class MainWindow:
    default_list = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple']

    def __init__(self, master):
        self.init_first_listbox(master)
        self.init_buttons(master)
        self.init_second_listbox(master)

    def init_first_listbox(self, master):
        self.listbox1 = Listbox(master)
        self.listbox1.pack(side=LEFT)

    def init_buttons(self, master):
        self.buttons_frame = Frame(master)
        self.buttons_frame.pack(side=LEFT)
        self.button_to_right = Button(self.buttons_frame, text=">>>")
        self.button_to_left = Button(self.buttons_frame, text="<<<")
        self.button_to_right.pack(side=TOP)
        self.button_to_left.pack(side=TOP)

    def init_second_listbox(self, master):
        self.listbox2 = Listbox(master)
        self.listbox2.pack(side=LEFT)

    def move_to_right(self):
        pass

    def move_to_left(self):
        pass
main()