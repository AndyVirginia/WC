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
from os.path import isdir, join
from os import listdir, getcwd
from re import match


class FileTypeError(BaseException):
    '''文件类型错误'''
    pass


class ArgvError(BaseException):
    '''命令行参数错误'''
    pass


class ArgvNotFoundError(BaseException):
    '''找不到命令行参数错误'''
    pass

def words(List):
    pass

def chars(List):
    pass

def solve_individual_file(path,command):
    des = ''
    with open(path) as File:
        lines= File.readlines()
        if '-l' in command:
            des1 = '行数：{0}行\n'.format(len(lines))
            des += des1
            if '-a' in command:
                pass
        elif '-a' in command:
            pass
        if '-w' in command:
            pass
        if '-c' in command:
            pass

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
            if '-l' in command:
                pass
            elif '-w' in command:
                pass
            elif '-c' in command:
                pass
    print(infomation)


def dir_list(path=getcwd()):
    L = []
    l = listdir(path)
    for x in l:
        if isdir(x):
            L.append(dir_list(x))
        else:
            L.append(x)
    return L


def is_file(name):
    '''
        判定一个命令行参数是不是文件名
    '''
    if match('-[sxalwc]', name):
        # 是不是所要的命令行参数
        return False
    elif match('[a-zA-z0-9_]*\.[a-zA-z0-9_]*', name):
        if match('[a-zA-z0-9_]*\.cpp', name):
            return True
        else:
            raise FileTypeError('无法处理的文件类型')
    else:
        raise ArgvError('无效的命令行参数')


def classify_command(argv):
    '''
        命令行参数分类
    '''
    if len(argv) == 0:
        raise ArgvNotFoundError
    command = []
    file_list = []
    for x in set(argv):
        if is_file(x):
            file_list.append(x)
        else:
            command.append(x)
    return command, file_list


if __name__ == '__main__':
    main()
