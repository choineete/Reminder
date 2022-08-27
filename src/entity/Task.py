from datetime import datetime


class Task:
    title = ''
    content = ''
    expireTime = datetime.now()

    def print(self):
        print(
            '标题: ' + self.title + '\n' + '内容: ' + self.content + '\n' + '过期时间: ' + self.expireTime.strftime('%Y/%m/%d'))


if __name__ == '__main__':
    task = Task()
    task.expireTime = datetime.now()
    task.print()
