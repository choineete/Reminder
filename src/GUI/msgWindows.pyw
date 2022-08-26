import ttkbootstrap as ttkb
from tkinter import *
from tkinter.ttk import *

# 新建主窗体
# root = Tk()
root = ttkb.Window(themename="journal")

# 获取屏幕大小消息
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# 设置窗口大小
width = screenWidth / 5
height = screenHeight / 5

# 构造窗体大小及位置
winSize = '%dx%d+%d+%d' % (width, height, (screenWidth - width) - 18, 10)

root.title('  您的周计划即将过期')
root.config(background='#FFFFFF')
root.iconbitmap('remind.ico')
root.geometry(winSize)
root.resizable(0, 0)

root.attributes("-topmost", -1)

# photo = PhotoImage('icon001.ico')

Separator(root).pack(fill=X)

Separator(root).pack(fill=X)

ttkb.Button(root, text="计划1", padding=8, bootstyle='danger').pack(fill=X)

Separator(root, bootstyle='warning').pack(fill=X)

ttkb.Button(root, text="计划2", padding=8, bootstyle='danger').pack(fill=X)

# 移除按钮操作
# button.destroy()

root.mainloop()
