from tkinter import *


def main():
    root = Tk()
    m = MainWindow(root)
    root.mainloop()


class MainWindow:
    product_list = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple']

    def __init__(self, master):
        self.init_first_listbox(master)
        self.init_buttons(master)
        self.init_second_listbox(master)

    def init_first_listbox(self, master):
        self.listbox1 = Listbox(master, selectmode=EXTENDED)
        self.listbox1.pack(side=LEFT)
        for product in self.product_list:
            self.listbox1.insert(END, product)

    def init_buttons(self, master):
        self.buttons_frame = Frame(master)
        self.buttons_frame.pack(side=LEFT)
        self.button_to_right = Button(self.buttons_frame, text=">>>", command=self.move_to_right)
        self.button_to_left = Button(self.buttons_frame, text="<<<", command=self.move_to_left)
        self.button_to_right.pack(side=TOP)
        self.button_to_left.pack(side=TOP)

    def init_second_listbox(self, master):
        self.listbox2 = Listbox(master, selectmode=EXTENDED)
        self.listbox2.pack(side=LEFT)

    def move_to_right(self):
        select = list(self.listbox1.curselection())
        for i in select:
            self.listbox2.insert(END, self.listbox1.get(i))
        select.reverse()
        for i in select:
            self.listbox1.delete(i)

    def move_to_left(self):
        select = list(self.listbox2.curselection())
        for i in select:
            self.listbox1.insert(END, self.listbox2.get(i))
        select.reverse()
        for i in select:
            self.listbox2.delete(i)


main()
