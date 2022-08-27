import tkinter as tk
import sched
import time


class MyApp(object):
    def __init__(self, parent):
        self.root = parent
        self.root.geometry('400x300')

        btn = tk.Button(parent, text='Hide', command=self.onClick)
        btn.pack()

        self.scheduler = sched.scheduler(time.time, time.sleep)

    def onClick(self):
        self.hide()
        self.scheduler.enter(3, 1, self.show, ())
        self.scheduler.run()

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.deiconify()

if __name__ == '__main__':
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()