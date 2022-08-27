class User:
    emp_num = ''
    name = ''

    def __init__(self,
                 emp_num='',
                 name=''):
        self.emp_num = emp_num
        self.name = name

        print('创建用户 ' + name)
