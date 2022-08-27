from plyer import notification
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# notify(title='', message='', app_name='', app_icon='', timeout=10, ticker='', toast=False)
# 用于弹出通知框
# title 通知框标题， message 通知内容， app_icon 弹窗图标
def notify(title, message):
    notification.notify(title=title, message=message, app_name="周计划提醒系统",
                        app_icon='icon000.ico', timeout=10, ticker='111', toast=False)


# if __name__ == '__main__':
#     notify("标题", "消息", "D:/DP1_ProjectsDeveloping/PythonProjects/winNotify/icon000.ico")


