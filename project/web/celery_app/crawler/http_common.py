# coding=utf-8
# Copyright Sangfor. All rights reserved

'''
http/https操作通用接口
'''

import requests
from celery_app.crawler import exceptions as comm_ex

requests.packages.urllib3.disable_warnings()


def get_http_header(host,  cookie=None):
    '''
    获取http请求头
    :param host:  host
    :param cookie:
    :return:
    '''

    header = {}
    header[
        'Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    header['Accept-Encoding'] = 'gzip, deflate, br'
    header['Accept-Language'] = 'zh-CN,zh;q=0.9'
    header['Connection'] = 'keep-alive'
    if cookie:
        header['Cookie'] = cookie

    header['Host'] = host
    header['Upgrade-Insecure-Requests'] = '1'
    header[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    return header


def https_get_html(url, host, cookie=None):
    '''
     https请求
    :param url:
    :param host:
    :param cookie:
    :return: 返回html页面
    '''

    headers = get_http_header(host, cookie)
    res = requests.get(url, headers=headers, verify=False)
    if res.status_code != 200:
        raise comm_ex("请求{}失败，错误码：{}".format(url, res.status_code))
    return str(res.content)


def main():
    html_content = https_get_html(
        'https://www.baidu.com/s?wd=%e4%bc%a0%e5%a5%87%e7%a7%81%e6%9c%8d', 'www.baidu.com')

    print(html_content)

if __name__ == '__main__':
    main()
