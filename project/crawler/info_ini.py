# coding=utf-8
# Copyright Sangfor. All rights reserved

'''
配置读取
'''

import ConfigParser
import const

class KeyIniObj:
    '''
    关键字类对象
    '''
    def __init__(self):
        self.keyword = ''
        self.start_page = 0
        self.end_page = 3


class InfoIniObj:
    def __init__(self):
        self.key_list = []      #关键字列表
        self.step = 0           #当前运行的步骤

def read_info_ini():
    '''
    读取配置
    :return:
    '''
    conf = ConfigParser.ConfigParser()
    conf.read(const.INFO_INI_FILE)

    info_obj = InfoIniObj()
    cnt = int(conf.get('keyword','keyword_cnt'))
    for i in range(0, cnt):
        key_obj = KeyIniObj()
        key_obj.keyword = conf.get('keyword', 'keyword{}'.format(i))
        key_obj.start_page = int(conf.get('keyword', 'start_page{}'.format(i)))
        key_obj.end_page = int(conf.get('keyword', 'end_page{}'.format(i)))
        info_obj.key_list.append(key_obj)

    info_obj.step = int(conf.get('sys','step'))
    return info_obj

def upd_info_ini(info_obj):
    '''
    更新step
    :param info_obj: info_obj对象
    :return:
    '''

    config = ConfigParser.ConfigParser()
    config.add_section("keyword")

    cnt = len(info_obj.key_list)
    i = 0
    config.set('keyword','keyword_cnt', str(cnt))
    for key_info in info_obj.key_list:
        config.set('keyword', 'keyword{}'.format(i), key_info.keyword)
        config.set('keyword', 'start_page{}'.format(i), str(key_info.start_page))
        config.set('keyword', 'end_page{}'.format(i), str(key_info.end_page))
        i = i + 1

    config.add_section("sys")
    config.set('sys','step', str(info_obj.step))
    config.write(open(const.INFO_INI_FILE, "w"))


def main():
    read_info_ini()

if __name__ == '__main__':
    main()
