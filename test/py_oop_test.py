import string
from datetime import *


class User:
    name = string
    emp_num = string

    def __init__(self, emp_num='', name=''):
        self.emp_num = emp_num
        self.name = name


class Task:
    title: string
    content: string
    plan_date: datetime

    # 为什么这样设置plan_date呢？ 为了保证，既没有传入日期值也没有传入剩余天数时，message中的天数为一个异常值
    def __init__(self, title='', content='', plan_date=datetime.now() + timedelta(days=-9999)):
        self.title = title
        self.content = content
        self.plan_date = plan_date


class Message:
    user: User
    task: Task
    # 剩余天数
    remaining_days: int
    # 苍穹云发过来的提醒消息
    remind_content: string

    def __init__(self, user: User, task: Task, remind_content='', remaining_days=-9999):
        self.user = user
        self.task = task
        self.remind_content = remind_content

        # 根据 remaining_days 是否传值来决定，remaining_days的计算方式
        if remaining_days == -9999:
            self.remaining_days = (task.plan_date - datetime.now()).days
        else:
            self.remaining_days = remaining_days

    # 模式0 通过msg的task信息动态生成消息
    # 模式1 直接返回苍穹传过来的消息
    def create_message(self, mode: int):
        if mode == 0:
            message = ''
            title = self.task.title
            plan_date = self.task.plan_date.strftime('%Y-%m-%d')

            if self.remaining_days == 1:
                message = f'你好，你的周计划【{title}】将于{plan_date}到期，请及时提交成果物，谢谢！'
            elif self.remaining_days == 0:
                message = f'你好，你的周计划【{title}】今天到期，请及时提交成果物，谢谢！'
            elif -7 < self.remaining_days < 0:
                message = f'你好，你的周计划【{title}】于{plan_date}到期、已逾期{-self.remaining_days}天，请及时提交成果物，谢谢！'
            elif self.remaining_days < -6:
                message = f'你好，你的周计划【{title}】于{plan_date}到期，已逾期{-self.remaining_days}天，超时完成将不计入条数，请及时提交成果物，谢谢！'
            print("通过Task制作获取计划逾期信息")
        else:
            print("直接从苍穹云获取计划逾期信息")
            message = self.remind_content

        return message


if __name__ == '__main__':
    print(Message(User(), Task()).create_message(1))
