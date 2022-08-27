import datetime

from src.entity.Task import Task
from src.entity.User import User


class Message:
    serial_num = 0
    user = User()
    task = Task()
    create_date = datetime.datetime.now()

    def __init__(self,
                 serial_num=0,
                 user=User(),
                 task=Task(),
                 create_date=datetime.datetime.now()
                 ):
        self.serial_num = serial_num
        self.user = user
        self.task = task
        self.create_date = create_date

        print("创建消息 " + str(serial_num))
