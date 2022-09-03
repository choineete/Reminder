import os
import sys

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
    # width = 320
    # height = 420
    width = 500
    height = 700

    # 构造窗体大小及位置
    root_size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) - 18, 10)

    root.title('')
    root.config(background='#FFFFFF')
    root.iconbitmap(icon_filename)
    root.geometry(root_size)
    # root.resizable(0, 0)
    root.attributes("-topmost", -1)

    # 重新定义点击关闭按钮的处理，不退出进程，隐藏窗体
    root.protocol('WM_DELETE_WINDOW', lambda: root.withdraw())

    return root


# 为每条消息创建一个框
# 参数分别是 父容器 消息文本 消息编号
def create_message_item(root_frame, msg, num):

    # 创建消息UI主体
    frame = tk.Frame(root_frame)


    # 效果1：提醒消息
    label_2 = tk.Label(frame,
                       text=msg,
                       fg='#535353',
                       font=('微软雅黑', 10, 'bold'))
    label_2.pack()

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
