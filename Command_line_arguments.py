#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Command_line_arguments.py
@Time    :   2019/02/19 15:58:41
@Author  :   Andy Virginia 
@Version :   1.0
@Contact :   1049955895@qq.com
@Desc    :   None
'''

# here put the import lib
from os import getcwd, listdir
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
