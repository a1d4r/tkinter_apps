from tkinter import *


def main():
    root = Tk()
    m = MainWindow(root)
    root.mainloop()


class MainWindow:
    def __init__(self, master):
        self.init_entry(master)
        self.init_listbox(master)

    def init_entry(self, master):
        self.entry = Entry(master)
        self.entry.pack(side=TOP)
        self.entry.bind("<Return>", self.move_to_listbox)

    def init_listbox(self, master):
        self.listbox = Listbox(master)
        self.listbox.pack(side=TOP)
        self.listbox.bind("<Double-Button-1>", self.move_to_entry)

    def move_to_listbox(self, event):
        print('move_to_listbox')
        line = self.entry.get()
        self.listbox.insert(END, line)
        self.entry.delete(0, END)

    def move_to_entry(self, event):
        print('move_to_entry')
        line = self.listbox.get(self.listbox.curselection())
        print(type(line))
        self.entry.delete(0, END)
        self.entry.insert(0, line)
        self.listbox.delete(self.listbox.curselection())


main()
