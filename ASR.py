# -*- coding: utf-8 -*-
# author:And370
# time:2020/7/1

from aip import AipSpeech

from config import APP_ID, API_KEY, SECRET_KEY


client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 识别本地文件
res = client.asr(get_file_content('./audio/output.wav'), 'pcm', 16000, {'dev_pid': 1537, })

print(res)
