from datetime import datetime


class Task:
    title = ''
    content = ''
    expire_time = datetime.now()
    remaining_days = -1

    def __init__(self,
                 title='',
                 content='',
                 expire_time=datetime.now(),
                 remaining_days=-1,
                 ):
        self.title = title
        self.content = content
        self.expire_time = expire_time
        self.remaining_days = remaining_days

        if self.remaining_days == -1:
            self.remaining_days = (expire_time - datetime.now()).days
        print('创建任务' + title)
