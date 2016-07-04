import time
import threading

source_list = []

lock = threading.Lock()


class Thread1(threading.Thread):
    def run(self):
        # lock.acquire()

        for index in range(0, 10):
            value = "{0}:{1}".format("Thread 1", index)
            source_list.append(value)

            time.sleep(1)

            print(value)

        # lock.release()


class Thread2(threading.Thread):
    def run(self):
        # lock.acquire()

        for index in range(0, 10):
            value = "{0}:{1}".format("Thread 2", index)
            source_list.append(value)

            time.sleep(2)

            print(value)
        # lock.release()


t1 = Thread1()
t2 = Thread2()

t1.start()
t2.start()

t1.join()
t2.join()

print("*" * 80)
print(source_list)
print("*" * 80)
