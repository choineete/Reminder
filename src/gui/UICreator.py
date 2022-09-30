import os
import sys
import webbrowser
from tkinter import messagebox

import pystray
import ttkbootstrap as ttk
import tkinter as tk



# 弹窗显示任务详情
from PIL import Image
from pystray import MenuItem, Menu
from ttkbootstrap.dialogs import MessageDialog, Messagebox
from ttkbootstrap.icons import Icon

from data.data_acquier import get_result, make_message_list, get_params


# 打包时图片路径
# icon_filename = exe_get_picture('img', 'remind.ico')
# 开发时路径
icon_filename = './img/remind.ico'


def restart_program():
    print('ready to restart program......')
    python = sys.executable
    os.execl(python, python, *sys.argv)
    sys.exit()

def refresh(root:ttk.Window):
    # 清空root里的全部子元素

    # 不能这样迭代删除，必须通过key取出元素再删除
    # for old_frame in root.children.values():
    #     old_frame.destroy()

    for key in list(root.children.keys()):
        root.children[key].destroy()

    # 消息的容器
    root_frame = create_root_frame(root)
    # 按钮的容器
    btn_frame = create_root_frame(root)

    # 请求数据，返回结果字典
    params = get_params()
    result = get_result(params)

    # 请求成功，才去构造消息列表，否则弹出警告消息
    if result is not None:
        # 构造消息列表
        msg_list = make_message_list(result)
        for i in range(0, len(msg_list)):
            create_message_item(root_frame=root_frame, msg=msg_list[i])
        create_btns(btn_frame, 1, root)
    else:
        create_message_item(root_frame=root_frame, msg='请求消息失败，请检查网络或稍后尝试重启应用')
        create_btns(btn_frame, 0, root)
    name = MessageDialog(message='刷新成功',
                       title=' ',
                       buttons=['OK'],
                       alert=True,
                       icon=Icon.info
                       ).image_names()
    print(name)

    messagebox.showinfo(title=None, message='刷新成功', icon='info')
    root.update()



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


def show_task_detail(title, content, expire_time, root_frame):
    screenwidth = root_frame.master.winfo_screenwidth() / 2.3
    screenheight = root_frame.master.winfo_screenheight() / 2.3

    position = (int(screenwidth), int(screenheight))

    mb = MessageDialog(message=content + '\n' + '到期时间： ' + expire_time,
                       title=title,
                       buttons=['OK'],
                       alert=True,
                       ).show(position)


def set_root_center(root):
    root.update()
    # 获取屏幕大小消息
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()

    # 获取窗口大小
    width = root.winfo_width()
    height = root.winfo_height()

    # 构造窗体大小及位置
    # root_size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) - 18, 10)
    root_size = '+%d+%d' % ((screenwidth - width) / 2, (screenheight - height) / 2)

    root.geometry(root_size)


# 创建主窗体
def create_root_window():
    root = ttk.Window()

    root.title('周计划提醒')
    root.config(background='#FFFFFF')
    root.iconbitmap(icon_filename)
    root.resizable(0, 0)
    root.attributes("-topmost", -1)

    # 重新定义点击关闭按钮的处理，不退出进程，隐藏窗体
    root.protocol('WM_DELETE_WINDOW', lambda: root.withdraw())

    return root


# 为每条消息创建一个框
# 参数分别是 父容器 消息文本 消息编号
def create_message_item(root_frame, msg, level):
    # 创建消息UI主体

    frame = tk.Frame(root_frame)

    # 效果1：显示消息类别
    type, color = get_type_and_color(level)
    # label_2 = tk.Label(frame,
    #                    text='今日到期',
    #                    background='#DC143C',
    #                    foreground='#DC143C',
    #                    font=('微软雅黑', 10, 'bold'))
    # label_2.pack(side='left')

    # 效果1：图片
    photo = tk.PhotoImage(file='./img/img.png')
    tk.Label(root_frame, image=photo).pack(side="left")

    # 效果2：提醒消息
    label_1 = tk.Label(frame,
                       text=msg,
                       bg='#535353',
                       font=('微软雅黑', 10, 'bold'))
    label_1.pack(side='left')

    frame.pack(pady='10px', padx='10px')

    return frame

def get_type_and_color(level):
    type_enum = {
        1 : '即将到期',
        2 : '今日到期',
        3 : '到期3日',
        4 : '到期7日'
    }
    color_enum = {
        1: '',
        2: '',
        3: '',
        4: ''
    }
    return type_enum[1], color_enum[1]


def create_btns(btn_frame: tk.Frame, mode, root):
    if mode == 1:
        # “去提交”按钮，打开苍穹平台
        ttk.Button(btn_frame,
                   text='去提交',
                   style='warning',
                   command=lambda: webbrowser.open_new_tab('https://club.kdcloud.com/')).grid(row=0, column=0)

        # 添加两按钮间的空格
        tk.Label(btn_frame, text='     ').grid(row=0, column=1)

        # ”知道了“按钮，撤回窗口到系统托盘
        ttk.Button(btn_frame,
                   text='知道了',
                   style='primary',
                   command=lambda: root.withdraw()).grid(row=0, column=2)
    else:
        ttk.Button(btn_frame,
                   text='关闭应用',
                   style='danger',
                   command=lambda: root.destroy()).grid(row=0, column=0)

        # 添加两按钮间的空格
        tk.Label(btn_frame, text='     ').grid(row=0, column=1)

        ttk.Button(btn_frame,
                   text='刷新',
                   style='danger',
                   command=lambda: refresh(root)).grid(row=0, column=2)




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
