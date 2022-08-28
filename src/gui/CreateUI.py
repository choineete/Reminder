import os
import sys
from tkinter.messagebox import showinfo

import pystray
import ttkbootstrap as ttk
import tkinter as tk

# 弹窗显示任务详情
from PIL import Image
from pystray import MenuItem, Menu
from ttkbootstrap.dialogs import MessageDialog


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 返回打包到exe文件中静态资源运行时的文件路径
def exe_get_picture(folder, filename):
    filename = resource_path(os.path.join(folder, filename))
    return filename


# 打包时图片路径
# icon_filename = exe_get_picture('img', 'remind.ico')
# 开发时路径
icon_filename = './img/remind.ico'


def show_task_detail(title, content, expire_time, root_frame):
    screenwidth = root_frame.master.winfo_screenwidth() / 2.3
    screenheight = root_frame.master.winfo_screenheight() / 2.3

    position = (int(screenwidth), int(screenheight))

    mb = MessageDialog(message=content + '\n' + '到期时间： ' + expire_time,
                       title=title,
                       buttons=['OK'],
                       alert=True,
                       ).show(position)


# 创建主窗体
def create_root_window():
    root = ttk.Window()

    # 获取屏幕大小消息
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()

    # 设置窗口大小
    width = 320
    height = 420

    # 构造窗体大小及位置
    root_size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) - 18, 10)

    root.title('')
    root.config(background='#FFFFFF')
    root.iconbitmap(icon_filename)
    root.geometry(root_size)
    root.resizable(0, 0)
    root.attributes("-topmost", -1)

    # 重新定义点击关闭按钮的处理，不退出进程，隐藏窗体
    root.protocol('WM_DELETE_WINDOW', lambda: root.withdraw())

    return root


# 为每条消息创建一个框
def create_message_item(root_frame, msg):
    # 消息序号
    num = msg.serial_num
    # 周计划标题和内容 *** 注意限制title长度
    task = msg.task
    title = task.title
    content = task.content
    # 剩余时间
    expire_time = '2022/08/27'
    days = msg.task.remaining_days

    # 创建消息UI主体
    frame = tk.Frame(root_frame)

    # 构建消息内容
    # 效果1：任务1  周计划提醒系统开发
    label_1 = tk.Label(frame,
                       text='任务' + str(num) + '  ' + title + '  ',
                       font=('微软雅黑', 9, 'bold'))
    label_1.grid(row=0, column=0)
    # 效果2：“查看详情”按钮
    detail_button = tk.Button(frame,
                              text='查看详情',
                              bg='#F0F0F0',
                              relief='ridge',
                              font=('微软雅黑', 8),
                              command=lambda: show_task_detail(title, content, expire_time, root_frame))
    detail_button.grid(row=0, column=1)
    # 效果3：距离过期时间，还剩
    label_2 = tk.Label(frame,
                       text='距离过期时间，还剩',
                       fg='#535353',
                       font=('微软雅黑', 8))
    label_2.grid(row=1, column=0, sticky='w')
    # 效果4：1天
    label_3 = tk.Label(frame,
                       text=str(days),
                       fg='red',
                       font=('微软雅黑', 8))
    label_3.place(relx=1,
                  rely=0,
                  in_=label_2,
                  bordermode=tk.OUTSIDE)
    label_4 = tk.Label(frame,
                       text='天',
                       fg='#535353',
                       font=('微软雅黑', 8))
    label_4.place(relx=1,
                  rely=0,
                  in_=label_3,
                  bordermode=tk.OUTSIDE)

    frame.pack(pady='10px')

    return frame


# 创建装载所有消息的父容器
def create_root_frame(root):
    root_frame = tk.Label(root)
    root_frame.pack()
    return root_frame


# 创建系统托盘
def create_sys_tray(root):
    # 系统托盘菜单
    menu = (MenuItem('任务详情',
                     lambda: root.deiconify(),
                     default=True),

            Menu.SEPARATOR,

            MenuItem('退出',

                     lambda: root.destroy()))
    # 托盘图标
    image = Image.open(icon_filename)
    # 创建
    icon = pystray.Icon("周计划提醒",
                        image,
                        "周计划提醒",
                        menu)
    return icon
