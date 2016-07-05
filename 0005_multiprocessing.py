import time
import random
from multiprocessing import Pool


def do_someting(a):
    print "Copy file {0}".format(a)

    time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    files = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"]

    pool = Pool(2)
    pool.map(do_someting, files)
    pool.close()
    pool.join()
