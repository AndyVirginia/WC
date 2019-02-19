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



def words(List):
    '''
        单词数统计
    '''
    pass


def chars(List):
    '''
        字符数统计
    '''
    pass


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
            pass
        if '-c' in command:
            pass
