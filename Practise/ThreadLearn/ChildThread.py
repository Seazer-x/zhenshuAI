import threading
import time

threading.current_thread().name = "主线程"


def display():
    for i in range(1, 4):
        print(threading.current_thread().name, i)
        time.sleep(1)


t1 = threading.Thread(target=display, name="线程t1")
t1.start()
t1.join()

for item in range(1, 3):
    print(threading.current_thread().name, item)
    time.sleep(1)

threadLock = threading.Lock()


# class MyTread(threading.Thread):
#     def run(self):
#         print("开启线程", threading.current_thread().name)
#         threadLock.acquire()
#         for i in range(1, 5):
#             print(threading.current_thread().name)
#         threadLock.release()
#
#
# t1 = MyTread()
# t2 = MyTread()
# t3 = MyTread()
# t1.start()
# t2.start()
# t3.start()
