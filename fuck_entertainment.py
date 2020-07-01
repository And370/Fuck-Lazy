# -*- coding: utf-8 -*-
# author:And370
# time:2020/7/2
# 进程检测模块，主要用于封杀娱乐项目。
# 用win32或者psutil实现

import win32com.client

def check_exsit(process_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name like "%{}%"'.format(process_name))
    if len(processCodeCov) > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    res = check_exsit('qq.exe')
    print(res)
