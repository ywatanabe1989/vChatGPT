#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: "2023-03-24 19:56:27 (ywatanabe)"

import readchar
import threading
# from threading import Thread
import time


def waitKey():
    key = "x"
    while key != "q":
        print(key)
        key = readchar.readchar()
    event.set()
    # raise Exception


def count():
    counter = 0
    while True:
        print(counter)
        time.sleep(1)
        counter += 1
        if event.is_set():
            break


# class ThreadWithReturnValue(Thread):
#     def __init__(
#         self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None
#     ):
#         Thread.__init__(self, group, target, name, args, kwargs)
#         self._return = None

#     def run(self):
#         if self._target is not None:
#             self._return = self._target(*self._args, **self._kwargs)

#     def join(self, *args):
#         ### fixme
#         Thread.join(self, *args)
#         return self._return

#         # try:
#         #     Thread.join(self, *args)
#         #     return self._return
#         # except KeyboardInterrupt:
#         #     print("\nKeyboard Interruption during joining.\n")  #  Saved to: {spath}
#         #     return None


t1 = threading.Thread(target=waitKey)
t2 = threading.Thread(target=count)

t1.start()
t2.start()

# # t1_out = False
# while True:
#     try:
#         t1_out = t1.join()
#     except Exception as e:
#         t2.join()
#         print(e)
    

# # t2.join()

event = threading.Event()
t2.join()
