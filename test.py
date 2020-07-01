# -*- coding: utf-8 -*-
# author:And370
# time:2020/7/2

import psutil

print(psutil.pids())
for i in psutil.pids():
    print(psutil.Process(i))

