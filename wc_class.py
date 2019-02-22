#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   wc_class.py
@Time    :   2019/02/20 10:57:33
@Author  :   Andy Virginia 
@Version :   1.0
@Contact :   1049955895@qq.com
@Desc    :   None
'''

# here put the import lib
import sys
from os import getcwd, listdir
from os.path import isdir, isfile, join
from re import match, findall, compile, search


class WordCounter():

    def __init__(self, command):
        self.tra = False
        self.classify_command(command)
        if self.tra:
            self.traverse()
        else:
            self.wc_process()
        print(self.message)

    def classify_command(self, command):
        '''命令行参数分类'''
        self.com, self.file_list = [], []
        if '-x' in command:
            print('图形界面启动中。。。')
            return
        elif '-s' in command:
            print('遍历目录')
            self.tra = True
        file_pattern = compile('[a-zA-Z0-9_]+\.\w+')
        com_pattern = compile('-[cwla]')
        for x in command:
            if match(com_pattern, x):
                self.com.append(x)
            elif match(file_pattern, x):
                self.file_list.append(x)

    def wc_process(self):
        '''逐个查询目标文件的信息'''
        for x in self.file_list:
            FileInformation(self.com, x)

    def traverse(self, path=None):
        '''遍历'''
        self.message = ''
        for x in listdir(path):
            if isfile(x):
                f = FileInformation(self.com, x)
                self.message += f.info
            elif isdir(x):
                self.traverse(x)


class FileInformation():

    def __init__(self, opt, filename):
        self.opt = opt
        self.file = filename
        with open(filename, encoding='utf-8') as f:
            l = f.readlines()
            self.words(l)
            self.chars(l)
            self.line(l)
        self.create_info()

    def create_info(self):
        line = False
        self.info = '文件：\t{0}\n'.format(self.file)
        if '-w' in self.opt:
            self.info += '单词数：\t{0}\n'.format(self.word_num)
        if '-c' in self.opt:
            self.info += '字符数：\t{0}\n'.format(self.char_num)
        if '-l' in self.opt:
            self.info += '行数：\t{0}\n'.format(self.comment_line +
                                      self.space_line+self.code_line)
            line = True
        if '-a' in self.opt:
            des = '代码行：\t{0}\n注释行:\t{1}\n空行:\t{2}\n\n'.format(
                self.code_line, self.comment_line, self.space_line)
            if line:
                self.info += des
            else:
                self.info += '行数：\t{0}\n'.format(self.comment_line +
                                          self.space_line+self.code_line)+des

    def words(self, List):
        '''
            单词数统计
        '''
        word_pattern = compile('\w+\w')
        self.word_num = 0
        for line in List:
            self.word_num += len(findall(word_pattern, line))

    def chars(self, List):
        '''
            字符数统计
        '''
        char_pattern = compile('[a-zA-Z]')
        self.char_num = 0
        for line in List:
            self.char_num += len(findall(char_pattern, line))

    def file_process(self):
        '''
            文件处理主函数
        '''
        pass

    def line(self, List):
        '''
            行数统计
        '''
        block = False
        self.space_line = 0
        self.comment_line = 0
        self.code_line = 0
        line_comment_pattern = compile('.?//')
        left_comment_pattern1 = compile('.?/\*.*')
        left_comment_pattern2 = compile('.+/\*.*')
        right_comment_pattern = compile('.*\*/')
        for x in List:
            if block:
                if match(right_comment_pattern, x):
                    block = False
                self.comment_line += 1
            else:
                if len(x) <= 1:
                    self.space_line += 1
                elif left_comment_pattern1.match(x):
                    self.comment_line += 1
                    block = True
                elif left_comment_pattern2.search(x):
                    block = True
                    self.code_line += 1
                elif line_comment_pattern.match(x):
                    self.comment_line += 1
                else:
                    self.code_line += 1


if __name__ == "__main__":
    WordCounter(['-s', '-a', '-w','-l', ])
