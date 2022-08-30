from threading import Timer

def p():
    print("exec")

if __name__ == '__main__':
        t = Timer(1, p)
        t.start()
