#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   individual_file.py
@Time    :   2019/02/19 15:24:51
@Author  :   Andy Virginia 
@Version :   1.0
@Contact :   1049955895@qq.com
@Desc    :   None
'''

# here put the import lib
from re import findall, search, match


def additional__line(List, type='c/c++'):
    '''
        根据程序语言种类返回行数详细信息
    '''
    comments = 0
    codes = 0
    spaces = 0
    for line in List:
        if search('', line):
            pass
        elif search('', line):
            pass
        else:
            pass


def words(List):
    '''
        单词数统计
    '''
    s = 0
    for line in List:
        s += len(findall('^[a-zA-Z0-9]+$', line))
    return '单词数：{0}个\n'.format(s)


def chars(List):
    '''
        字符数统计
    '''
    c = 0
    for line in List:
        c += len(findall('[a-zA-z0-9]', line))
    return '字符数：{0}个'.format(c)


def solve_individual_file(path, command):
    des = ''
    with open(path) as File:
        lines = File.readlines()
        if '-l' in command:
            des1 = '行数：{0}行\n'.format(len(lines))
            des += des1
            if '-a' in command:
                pass
        elif '-a' in command:
            pass
        if '-w' in command:
            des += words(lines)
        if '-c' in command:
            des += chars(lines)
    return des


if __name__ == "__main__":
    print(solve_individual_file('test.py', ['-c', ]))
