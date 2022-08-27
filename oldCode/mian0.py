import tkinter as tk
from tkinter.messagebox import showinfo

import ttkbootstrap as ttk

from src.entity.Msg import Msg
from src.entity.Task import Task

import threading
import pystray
from PIL import Image
from pystray import MenuItem, Menu


def quit_window(icon: pystray.Icon):
    icon.stop()
    root.destroy()


def show_window():
    root.deiconify()


def on_exit():
    root.withdraw()


def showTaskDetail(msg):
    showinfo(title=msg.task.title,
             message=msg.task.content + '\n' + '          到期时间： ' + '2022/08/26')

# 创建主窗体
def UI_MakeRootWindows():
    root = ttk.Window()

    # 获取屏幕大小消息
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    # 设置窗口大小
    width = 280
    height = 400

    # 构造窗体大小及位置
    winSize = '%dx%d+%d+%d' % (width, height, (screenWidth - width) - 18, 10)

    root.title('')
    root.config(background='#FFFFFF')
    root.iconbitmap('remind.ico')
    root.geometry(winSize)
    root.resizable(0, 0)
    root.attributes("-topmost", -1)

    return root

# 创建消息UI
def UI_MakeMsgItem(root, msg):

    taskNum = msg.msgId
    taskTitle = msg.task.title
    days = 1

    frame = tk.Frame(root)

    label1 = tk.Label(frame, text='任务' + str(taskNum) + '  ' + taskTitle + '  ', font=('微软雅黑', 9, 'bold'))
    label1.grid(row=0, column=0)
    detailButton = tk.Button(frame, text='查看详情', bg='#F0F0F0', relief='ridge', font=('微软雅黑', 8), command = lambda : showTaskDetail(msg))

    detailButton.grid(row=0, column=1)

    frontText = tk.Label(frame, text='距离过期时间，还剩', fg='#535353', font=('微软雅黑', 8))
    frontText.grid(row=1, column=0, sticky='w')

    num = tk.Label(frame, text=str(days), fg='red', font=('微软雅黑', 8))
    num.place(relx=1, rely=0, in_=frontText, bordermode=tk.OUTSIDE)

    timeUnit = tk.Label(frame, text='天', fg='#535353', font=('微软雅黑', 8))
    timeUnit.place(relx=1, rely=0, in_=num, bordermode=tk.OUTSIDE)

    frame.pack(pady='10px')



if __name__ == '__main__':
    root = UI_MakeRootWindows()

    task = Task()
    task.title = '周计划提醒系统开发'
    task.content = '为现有周计划系统开发一个能主动提醒用户的小弹窗'

    msg = Msg()
    msg.msgId = 1
    msg.task = task

    UI_MakeMsgItem(root, msg)

    task = Task()
    task.title = '合同履约系统迁移'
    task.content = '将原有合同履约系统迁移至金蝶云苍穹上'

    msg = Msg()
    msg.msgId = 2
    msg.task = task

    UI_MakeMsgItem(root, msg)

    menu = (MenuItem('任务详情', show_window, default=True), Menu.SEPARATOR, MenuItem('退出', quit_window))
    image = Image.open("../src/gui/remind.ico")
    icon = pystray.Icon("icon", image, "周计划提醒", menu)

    # 重新定义点击关闭按钮的处理
    root.protocol('WM_DELETE_WINDOW', on_exit)


    threading.Thread(target=icon.run, daemon=True).start()
    root.mainloop()



