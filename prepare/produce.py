#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path


class PinYin(object):
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file


    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        f_obj = open(self.dict_file, "r")
        for f_line in f_obj.readlines():
            try:
                line = f_line.split('    ')
                self.word_dict[line[0]] = line[1]
            except:
                line = f_line.split('   ')
                self.word_dict[line[0]] = line[1]
        f_obj.close()


    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance(string, type('s')):
            string = string.decode("utf-8")
        
        for char in string:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return result


    def hanzi2pinyin_split(self, string="", split=""):
        result = self.hanzi2pinyin(string=string)
        if split == "":
            return result
        else:
            return split.join(result)


converter = PinYin()
converter.load_word()

input = open("tar.txt", "r")
output = open("py.txt", "w")
for line in input:
    line = line[:-1]
    output.write(converter.hanzi2pinyin_split(string=line, split=" ") + "\n")

input.close()
output.close()
