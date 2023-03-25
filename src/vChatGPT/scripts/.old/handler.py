#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: "2023-03-24 01:36:30 (ywatanabe)"

import signal

# Register an handler for the timeout
def handler(signum, frame):
    print("Forever is over!")
    raise Exception("end of time")

def loop_forever():
    import time
    while 1:
        print("sec")
        time.sleep(1)

# Register the signal function handler
signal.signal(signal.SIGALRM, handler)

# Define a timeout for your function
signal.alarm(10)

try:
    loop_forever()
except Exception as e:
    print(e)
