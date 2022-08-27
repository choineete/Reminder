
from tkinter import Tk

import threading
import pystray
from PIL import Image
from pystray import MenuItem, Menu


def quit_window(icon: pystray.Icon):
    icon.stop()
    win.destroy()


def show_window():
    win.deiconify()


def on_exit():
    win.withdraw()



menu = (MenuItem('任务详情', show_window, default=True), Menu.SEPARATOR, MenuItem('退出', quit_window))
image = Image.open("remind.ico")
icon = pystray.Icon("icon", image, "周计划提醒", menu)
win = Tk()
win.geometry("500x300")

# 重新定义点击关闭按钮的处理
win.protocol('WM_DELETE_WINDOW', on_exit)

threading.Thread(target=icon.run, daemon=True).start()


win.mainloop()