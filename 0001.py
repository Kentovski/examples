import threading
import time


def clock(name, count, sleep_seconds=1):
    while count != 0:
        print("Thread № 1 {0}:  current time is {1}".format(name, time.ctime()))

        time.sleep(sleep_seconds)

        count -= 1


thread1 = threading.Thread(target=clock, args=("Thread 1", 10, 1))
thread1.start()

# thread2 = threading.Thread(target=clock, args=("Thread 2", 10, 1))
# thread2.start()
