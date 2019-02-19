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
from os import getcwd, listdir
from os.path import isdir, join

from individual_file import *
from Command_line_arguments import *


def main():
    # 主程序
    try:
        command, file_list = classify_command(sys.argv[1:])
    except FileTypeError:
        print('无法处理的文件类型。')
        sys.exit()
    except ArgvError:
        print('无效的命令行参数。')
        sys.exit()
    except ArgvNotFoundError:
        sys.exit()
    print(command, file_list)
    infomation = ''
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
    elif len(file_list) == 0:
        # 没有可处理的文件
        raise ''
    elif len(command) == 0:
        # 没有可处理命令
        pass
    else:
        # 处理基础命令
        for x in file_list:
            solve_individual_file(x, command)
    print(infomation)


if __name__ == '__main__':
    main()
