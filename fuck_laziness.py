# -*- coding: utf-8 -*-
# author:And370
# time:2020/7/19

import os
import psutil
import playsound
from config import entertainments, audio_path
import random
import pyaudio
import wave
import keyboard


class Fucker(object):
    """
    In order to fix the laziness which is a bug of mine,I create this laziness fucker to end the vicious spiral.
    """

    def __init__(self):
        # Check the file/directory if exist.
        self.CONFIG_PATH = "Config"
        self.CONFIG_LIST = "fuckers.cfg"
        self.PROVERBS_PATH = "proverbs.txt"
        for file in self.CONFIG_PATH, self.CONFIG_LIST, self.PROVERBS_PATH:
            if not os.path.exists(file):
                os.mkdir(file)

        # Loads proverbs.
        self.proverbs = self._proverbs(self.PROVERBS_PATH)

        # To detect processing.
        self.entertainments = entertainments

        self.configs = self._configs()

    def start(self):
        print(self.proverbs[random.randrange(0, len(self.proverbs))],
              "本程序主要负责完成您对您自己的监督,当前监督有如下模式:\n"
              "a.娱乐进程检测\n"
              "b.时间段监督\n")
        # To different branch depends on configurations exist.
        if self.configs:
            self.run()
        else:
            self.config()

    def run(self):
        pass

    def config(self):
        fucker_name = input("\n".join(["开始建立一个新程序。",
                                       "给你的Lazy-Fucker起一个名称:\n"]))
        while fucker_name in self.configs:
            fucker_name = input("名称已存在,请再次输入:\n")
        self.configs.append(fucker_name)
        os.mkdir(os.path.join(self.CONFIG_LIST, fucker_name))
        print("%s程序初始化成功,请添加你所要限制的娱乐进程名称并以回车结束(连续回车两次即结束):" % fucker_name)
        input_exe = True
        while input_exe:
            input_exe = input()
            self.entertainments.add(input_exe)


    def _configs(self):
        with open(self.CONFIG_LIST, encoding='utf-8') as config_list:
            config_list = config_list.read().splitlines()
        return config_list

    def _proverbs(self, filename):
        if os.path.exists(filename):
            with open(filename, encoding='utf-8') as proverbs:
                return proverbs.read().splitlines()

    def _recorder(self, filename, seconds=1, channels=1, rate=16000):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* 开始录音...以回车结束录音",
              "* recording...press Enter to end recording",
              sep="\n")

        frames = []

        while not keyboard.is_pressed(" "):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))

    def _fuck_entertainment(self):
        fuck_audios = [os.path.join(audio_path, i) for i in os.listdir(audio_path)]
        p_names = {psutil.Process(i).name().lower() for i in psutil.pids()}

        for fuck in self.entertainments:
            if fuck + '.exe' in p_names:
                while True:
                    playsound.playsound(fuck_audios[random.randrange(0, len(fuck_audios))])

    def _fuck_time_range(self):
        pass


if __name__ == '__main__':
    fuck = Fucker()
    fuck.start()
