#!/usr/bin/python3
import multiprocessing as mp
import os
from multiprocessing import Pool
from multiprocessing import Process


print("Checking for Cores...")
print("Number of Cores : ", mp.cpu_count())

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def spawn(num):
  print(num)


if __name__ == '__main__':
  for i in range(25):
    ## right here
    p = mp.Process(target=spawn, args=(i,))
    p.start()
    p.join()
