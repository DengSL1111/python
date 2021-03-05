# coding=utf-8
# Copyright Sangfor. All rights reserved

'''
公共函数
'''

import os
from celery_app.crawler import const

def dictkey_to_list(src_dict):
    '''
    保存指定内容到文件中
    :param filename: 文件名
    :param content: 文件内容
    :return:
    '''
    key_list = []
    for key, val in src_dict.items():
        key_list.append(key)

    return key_list

def save_file(filename, content):
    '''
    保存指定内容到文件中
    :param filename: 文件名
    :param content: 文件内容
    :return:
    '''
    fp = open(filename, 'w')
    fp.write(content)
    fp.close()

def read_file(filename):
    '''
    读取制动文件中的内容
    :param filename: 文件名
    :return: 文件内容
    '''
    fp = open(filename)
    content = fp.read()
    fp.close()
    return content

def save_collect_info(filename, dns_detail_info):
    '''
    保存收集的信息到cvs文件中
    :param filename: 文件名
    :return: 
    '''

    fp = open(filename, 'w')
    title = '"主机IP"\t"归属地"\t"主域名"\t"关联域名"\n'
    fp.write(title)
    for web_ip, host_info in dns_detail_info.items():
        content = '"{}"'.format(web_ip)
        content += '\t"{}"'.format(host_info['belong'])
        content += '\t"{}"'.format(','.join(comm.dictkey_to_list(host_info['dns_info'])))

        #关联域名
        link_dns = {}
        for dns_name, dns_info in host_info['dns_info'].items():
            for tmp_dns_name in dns_info['link_dns']:
                link_dns[tmp_dns_name] = {}

        content += '\t"{}"'.format(','.join(comm.dictkey_to_list(link_dns)))
        content += '\n'
        fp.write(content)

    fp.close()

def log_print(content):
    '''
    写日志
    '''
    print(content)
    fp = open(const.LOG_FILE, 'a+')
    fp.write(content + '\r\n')
    fp.close()


if __name__ == '__main__':
    log_print('aaaa')
    log_print('bbbb')
