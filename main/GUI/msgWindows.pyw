from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import *
# 新建主窗体
root = Tk()

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

photo = PhotoImage('remind.ico')

link0 = Label(root, bg='#000000', height=1)
link0.grid(row = 0,column =0)

link = Label(root, text='任务1', bg='#FFFFFF', font=('微软雅黑', 12), height=2)
link.grid(row = 1 ,column =0)

link1 = Label(root, text='任务2', bg='#FFFFFF', font=('微软雅黑', 12), height=2)
link1.grid(row = 2 ,column =0)

# b1 = Button(root, bg='#DC143C', fg='#FFFFFF', activebackground='#DC143C', activeforeground='#FFFFFF', text='任务1', relief=FLAT)
# b1.pack()


root.mainloop()
