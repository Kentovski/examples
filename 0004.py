import time
import os
from queue import Queue
import threading
import urllib.request as urllib2


class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            content = self._queue.get()

            if content == 'quit':
                break

            response = urllib2.urlopen(content)

        print('Bye byes!')


def run():
    urls = [
        'http://www.python.org',
        'http://www.scala.org',
        'http://www.google.com',
        'http://www.ya.ru',
        'http://www.vk.com',
        'http://mememachine.memeglobal.com',
        'http://www.facebook.com',
        'http://www.twitter.com',
    ]
    queue = Queue()
    worker_threads = build_worker_pool(queue, 5)
    start_time = time.time()

    # Add the urls to process
    for url in urls:
        queue.put(url)

    # Add the poison pillv

    for worker in worker_threads:
        queue.put('quit')

    for worker in worker_threads:
        worker.join()

    print('Done! Time taken: {}'.format(time.time() - start_time))


def build_worker_pool(queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue)
        worker.start()
        workers.append(worker)
    return workers


if __name__ == '__main__':
    run()
