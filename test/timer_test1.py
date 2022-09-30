'''
Created on 2013-7-31
@author: Eric
'''
import time
import threading


def timer_start():
    t = threading.Timer(1, test_func, ("Parameter1",))
    t.start()


def test_func(msg1):
    print("I'm test_func,", msg1)
    timer_start()


def timer2():
    timer_start()
    while True:
        time.sleep(1)


if __name__ == "__main__":
    timer2()