#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: "2023-03-24 00:53:04 (ywatanabe)"

from datetime import datetime, timedelta
import sched
import time


def def1(name):
    print(name)


now = datetime.now()
now = datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
comp = datetime(now.year, now.month, now.day, now.hour, 30)

diff = comp - now
print(diff)

if int(diff.days) >= 0:
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(diff.seconds, 1, def1, ("hoge", ))
    scheduler.run()
else:
    print("do nothing")
