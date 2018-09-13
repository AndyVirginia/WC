#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-05 22:33:10
# @Author  : 王锴 (1049955895@qq.com)
# @Version : $Id$
from optparse import OptionParser


def main():
    # 主程序
    parser = OptionParser()
    parser.add_option('-c','--char', dest = 'char', action = 'store',
                      default = False, help = 'only user to count chars')
    parser.add_option('-l', '--line', dest = 'line', action = 'store',
                      default = False, help = 'only user to count lines')
    parser.add_option('-w', '--word', dest = 'word', action = 'store',
                      default = False, help = 'only user to count words')
    parser.add_option('-a',  dest = 'type', action = 'store',
                      default = False, help = 'only user to count type of line')
    option, args  = parser.parse_args()

    if option.char:
        print(chars(option.char))
    elif option.line:
        print(lines(option.line))
    elif option.word:
        print(words(option.word))
    elif option.type:
        print(type(option.type))
    else:
        print('无效的命令行参数！')


def lines(args):
    ''' 返回文件 file.c 的行数'''
    try:
        with open(args,'r',encoding='UTF-8') as file:
            i = len(file.readlines())
            return i+1
    except FileNotFoundError:
        return '未找到该文件！'

def words(args):
    # 返回文件单词数
    try:
        with open(args,'r',encoding='UTF-8') as f:
            file = f.readlines()
            space_flag = False
            words_num = 0
            for x in file:
                for y in x:
                    if (y < 'A' or y >'Z') and (y < 'a' or y > 'z'):
                        space_flag = True
                    else:
                        if space_flag == True:
                            words_num += 1
                            space_flag = False
            return words_num
    except FileNotFoundError:
        return '未找到该文件！'


def chars(args):
    # 返回文件字符个数
    try:
        with open(args,'r',encoding='UTF-8') as f:
            file = f.readlines()
            num = 0
            for x in file:
                for y in x:
                    if (y >= 'A' and y <= 'Z') or (y >= 'a' and y <='z'):
                        num += 1
            return num
    except FileNotFoundError:
        return '未找到该文件！'

def type(args):
    space_line = 0
    comment_line = 0
    code_line = 0
    try:
        with open(args,'r',encoding='UTF-8') as file:
            mark_flag = False            # 双引号标记
            block_comment_flag = False   # 块注释标记
            for line in file.readlines():
                line_comment_flag = False    # 行注释标记
                code_num = 0    # 行代码字符数
                slash = False
                asterisk = False
                for char in line:
                    if char !=  ' ':
                        if block_comment_flag == False and line_comment_flag == False:
                            code_num += 1
                        if char == '\"' and not block_comment_flag:
                            # 当当前的字符不处于一条注释中时，对字符串进行判定
                            if mark_flag:
                                mark_flag = False
                            else:
                                mark_flag = True
                        elif char == '/' and not mark_flag and not block_comment_flag:
                            # 当当前不处于字符串和块注释中，对注释进行判定
                            if not slash:
                                slash = True
                            else:
                                line_comment_flag = True
                                code_num -= 2
                        elif slash and char == '*' and not mark_flag:
                            block_comment_flag = True
                            code_num -= 2
                        elif block_comment_flag and char == '*':
                            asterisk = True
                        elif asterisk:
                            if char == '/':
                                block_comment_flag = False
                                line_comment_flag = True
                if code_num > 1:
                    code_line += 1
                else:
                    if block_comment_flag or line_comment_flag:
                        comment_line += 1
                    else:
                        space_line += 1
        return '代码行：'+str(code_line)+'\n注释行：'+str(comment_line)+'\n空行:'+str(space_line)
    except FileNotFoundError:
        return '找不到该文件'
                            

if __name__ == '__main__':
    main()
