from threading import Timer

# 循环任务
def p():
    print("exec")
    t = Timer(1, p)
    t.start()

if __name__ == '__main__':
        t = Timer(1, p)
        t.start()
