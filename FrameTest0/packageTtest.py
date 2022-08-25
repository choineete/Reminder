import threading

from PIL import Image
from pystray import Icon as icon, Menu as menu, MenuItem as item

# 载入图标
image = Image.open("remind.ico")
# 消息和消息标题
message = '消息'
msgTitle = '消息标题'
expiringSoonNum = 1
expiredNum = 2


def myNotify():
    myIcon.notify(message, msgTitle)


myMenu = menu(
    item('💡 周计划提醒', myNotify),

    # 分隔符
    menu.SEPARATOR,

    item(
        '🗑 即将过期计划' + ' ' + str(expiringSoonNum), myNotify),
    item(
        '🗑 已经过期计划' + ' ' + str(expiredNum), myNotify),

    # 分隔符
    menu.SEPARATOR,

    item('❌ 退出', lambda icon: icon.stop())
)

# 新建Icon对象
myIcon = icon('test', image, title='周计划提醒', menu=myMenu)

if __name__ == '__main__':
    # 设置单独线程运行系统托盘
    threading.Thread(target=myIcon.run_detached()).start()

