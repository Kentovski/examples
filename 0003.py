import random
import threading

import time


class Queue(object):
    def __init__(self, size=5):
        self._size = size
        self._queue = []
        self._lock = threading.RLock()
        self._empty = threading.Condition(self._lock)
        self._full = threading.Condition(self._lock)

    def put(self, value):
        with self._full:
            while len(self._queue) >= self._size:
                self._full.wait()

            self._queue.append(value)
            self._empty.notify()

    def get(self):
        with self._empty:
            while len(self._queue) == 0:
                self._empty.wait()

            result = self._queue.pop(0)
            self._full.notify()
            return result


def processing_data(queue):
    number = 0
    while number >= 0:
        number = queue.get()

        print("Processing number {0}".format(number))

        print("Processing thread is sleeping")
        time.sleep(3)
        print("Processing thread is woken up")

    print("processing data is finished")


def generating_data(queue):
    for _ in range(0, 10):
        number = random.randint(1, 100)
        print("Put number {0}".format(number))
        queue.put(number)

    queue.put(-100)


queue1 = Queue(size=5)


t1 = threading.Thread(target=processing_data, args=(queue1,))
t2 = threading.Thread(target=generating_data, args=(queue1,))

t1.start()
t2.start()
