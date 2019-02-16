#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   wc.py
@Time    :   2019/02/02 16:55:45
@Author  :   Andy Virginia 
@Version :   2.0
@Contact :   1049955895@qq.com
@Desc    :   None
'''

# here put the import lib
import sys


def main():
    # 主程序
    command = sys.argv[1:]
    infomation = ''
    # print(command)
    # -c 字符数,
    # -w 单词数,
    # -l 行数,
    # -s 递归处理目录下文件,
    # -a 返回详细信息(注释行/空行/代码行)
    # -x 单独使用如果命令行这个参数，则程序显示图形界面
    if '-x' in command:
        # 开启图形界面
        pass
    elif '-s' in command:
        # 递归处理目录下.py文件
        pass
    else:
        fileName = command[-1]  # 文件名
        command = command[:-1]  # 真正的命令行
        secondarychoice(command, fileName)
    print(infomation)

def secondarychoice(command, name):
    '''次级选择'''
    line = ''
    if '-a' in command:
        # 输出详细信息
        pass
    else:
        if '-c' in command:
            # 输出字符数
            pass
        if '-w' in command:
            # 输出单词数
            pass
        if '-l' in command:
            # 输出行数
            

def lines(name):
    with open(name,mode = 'r',encoding = 'utf-8') as f:
        return len(f.readlines())

def words(name):
    pass

def char(name):
    pass

if __name__ == '__main__':
    main()
