# coding=utf-8
# Copyright Sangfor. All rights reserved

'''
通过百度关键字搜索，把对应的域名查询出来
'''

from urllib import quote,unquote
import http_common as http_comm
import comm

def get_baidu_keyword_dns_onepage(keyword, page):
    '''
    获取第几页的关键字域名
    :param keyword: 关键字
    :param page: 页数
    :return: html字符串
    '''
    hosts = 'www.baidu.com'
    page_index = page * 10
    url = 'https://www.baidu.com/s?{}&pn={}'.format(keyword, page_index)
    comm.log_print("url : {}".format(url))
    html_content = http_comm.https_get_html(url, hosts)
    return html_content


def rm_nouse_word(content):
    '''
    删除无用的单词
    :param content: 
    :return: content
    '''
    if content.find('<') < 0 and content.find('>') < 0:
        return content

    while(True):
        index = content.find('>')
        if index < 0:
            break
        content = content[index + 1:]

    return content


def parse_html_dns(html_content):
    '''
    解析html中的域名
    :param html_content: html内容
    :return: 域名列表
    '''

    dns_list = []
    while(True):
        start_flag = html_content.find('div class="f13')
        if start_flag <= 0:
            break

        html_content = html_content[start_flag:]
        start_flag = html_content.find('href="')
        html_content = html_content[start_flag:]
        start_flag = html_content.find('">')
        html_content = html_content[start_flag + 2:]
        end_flag = html_content.find('</a>')
        url_str = html_content[:end_flag]

        start_flag = url_str.find('/')
        if start_flag > 0:
            url_str = url_str[:start_flag]

        url_str = rm_nouse_word(url_str)
        # 简单判断是否为域名
        if url_str.count('.') >= 2:
            dns_list.append(url_str)

    return dns_list


def get_baidu_keyword_dns(info_list):
    '''
    通过百度关键字搜索，获取相关的域名
    :param key_word: 关键字
    :param start_page: 起始页
    :param end_page: 结束页
    :return: 域名列表
    '''

    dns_list = []
    for info_obj in info_list:
        key_word = info_obj.keyword
        start_page = info_obj.start_page
        end_page = info_obj.end_page
        keyword_dict = {'wd': key_word}
        keyword_urlcode = 'wd=' + quote(key_word,'utf-8')
        comm.log_print('查询关键字 ({})的域名,编码后关键字为 : {}'.format(key_word, keyword_urlcode))

        for i in range(start_page, end_page):
            html_content = get_baidu_keyword_dns_onepage(keyword_urlcode, i)
            html_content = html_content
            one_dns_list = parse_html_dns(html_content)

            dns_list += one_dns_list

    return dns_list
