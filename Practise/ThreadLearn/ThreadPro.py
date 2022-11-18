import threading
import time


class MyTread(threading.Thread):
    def __init__(self, name, count):
        super(MyTread, self).__init__()
        self.name = name
        self.count = count

    def run(self):
        print("线程", self.name, "启动")
        for i in range(1, self.count + 1):
            print(i, end="  ")
            time.sleep(1)


t1 = MyTread("T1", 3)
t2 = MyTread("T2", 4)
t3 = MyTread("T3", 5)
t1.start()
t2.start()
t3.start()
