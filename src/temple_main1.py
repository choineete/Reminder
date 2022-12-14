import threading
import ttkbootstrap

from data.data_acquier import get_params, get_result, make_message_list
from src.gui.UICreator import create_root_window, create_root_frame, create_sys_tray, create_message_item, \
    set_root_center, create_btns, create_type_btn, \
    create_type_root_frame, create_msg_root_frame

# 消息的紧急程度种类
LEVEL_DICT = {
    "long": 1,
    "short": 2,
    "today": 3,
    "soon": 4
}


def msg_refresh():
    root_frame.destroy()
    btn_frame.destroy()


# 循环提醒，设置提醒策略 frequency, root : ttkbootstrap.Window
# 窗口的3种状态
# normal 显示
# iconic 缩小到图标
# withdrawn 缩小到托盘
def remind_loop(loop_seconds, root: ttkbootstrap.Window):
    print("弹出频率" + str(loop_seconds) + "秒")
    print("当前窗口状态" + root.state())
    if root.state() != "normal":
        root.deiconify()
    threading.Timer(loop_seconds, remind_loop, (loop_seconds, root)).start()


# 根据不同的任务紧急程度设置 窗口弹出频率
def get_frequency(level_list):
    for i in level_list:
        if i == LEVEL_DICT["long"]:
            return 2
        elif i == LEVEL_DICT["short"]:
            return 5
        elif i == LEVEL_DICT["today"]:
            return 10
        elif i == LEVEL_DICT["soon"]:
            return 20
        else:
            return 1


if __name__ == '__main__':
    root = create_root_window()
    tray = create_sys_tray(root)
    # 获取用户工号，构建请求参数
    params = get_params()

    # 消息和其类型的父容器
    root_frame = create_root_frame(root)
    # 按钮的容器
    btn_frame = create_root_frame(root)

    # 消息的容器
    msg_root_frame = create_msg_root_frame(root_frame)
    # 消息类型的容器
    type_root_frame = create_type_root_frame(root_frame)

    # 请求数据，返回结果字典
    result = get_result(params)

    # 请求成功，才去构造消息列表，否则弹出警告消息
    if result is not None:
        # 构造消息列表
        msg_list, level_list = make_message_list(result)
        for i in range(0, len(msg_list)):
            create_message_item(msg_root_frame=msg_root_frame, msg=msg_list[i])
            create_type_btn(type_root_frame, level=level_list[i])
        create_btns(btn_frame, 1, root)
    else:
        create_message_item(msg_root_frame=msg_root_frame, msg='请求消息失败，请检查网络或稍后尝试重启应用')
        create_btns(btn_frame, 0, root)

    # 运行系统托盘
    threading.Thread(target=tray.run, daemon=True).start()
    # 设置提醒频率
    loop_seconds = get_frequency(level_list)
    threading.Thread(target=remind_loop, args=(loop_seconds, root), daemon=True).start()

    # 设置窗口居中
    set_root_center(root)
    root.mainloop()
