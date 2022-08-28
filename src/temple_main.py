import datetime
import os
import sys
import threading

from src.entity.Message import Message
from src.entity.Task import Task
from src.entity.User import User
from src.gui.CreateUI import create_root_window, create_root_frame, create_sys_tray, create_message_item



if __name__ == '__main__':
    root = create_root_window()
    tray = create_sys_tray(root)
    root_frame = create_root_frame(root)

    user = User('010200002082', '何燚')

    task1 = Task('周计划系统提醒功能开发', '为现有云苍穹上的周计划提醒系统开发windows提醒客户端程序', datetime.datetime.now(), 1)
    task2 = Task('合同履约系统苍穹云开发', '将现有合同履约系统搬移到苍穹云平台', datetime.datetime.now(), 2)

    msg1 = Message(1, user, task1)
    msg2 = Message(2, user, task2)

    msg_item1 = create_message_item(root_frame, msg1)
    msg_item2 = create_message_item(root_frame, msg2)


    threading.Thread(target=tray.run, daemon=True).start()
    root.mainloop()

