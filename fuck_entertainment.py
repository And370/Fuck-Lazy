# -*- coding: utf-8 -*-
# author:And370
# time:2020/7/2
# 进程检测模块，主要用于封杀娱乐项目。
# 用win32或者psutil实现

import os
import psutil
import playsound
from config import entertainments, audio_path
import random



fuck_audios = [os.path.join(audio_path, i) for i in os.listdir(audio_path)]
p_names = {psutil.Process(i).name().lower() for i in psutil.pids()}

for fuck in entertainments:
    if fuck + '.exe' in p_names:
        while True:
            playsound.playsound(fuck_audios[random.randrange(0,len(fuck_audios))])
