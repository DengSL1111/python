# coding=utf-8
# Copyright Sangfor. All rights reserved

'''
查询域名、ip、地域等信息
'''

import json
import socket
import http_common as http_comm
import comm


def get_ip_belong(ip):
    '''
    获取ip的归属地
    '''
    host = 'ip-api.com/json/'
    url = ' http://ip-api.com/json/{}'.format(ip)
    res = http_comm.https_get_html(url, host)
    res = res.replace("b\'", '')
    res = res.replace("\'", '')
    res_json = json.loads(res)
    belong = '{} - {}'.format(res_json.get('country'), res_json.get('city'))
    return belong


def get_dns_ip(dns_name):
    '''
    获取域名对应的ip
    :param dns_name:
    :return: 域名对应的IP
    '''
    web_ip = None
    try:
        res = socket.getaddrinfo(dns_name, None)
        web_ip = res[0][4][0]
    except Exception as ex:
        comm.log_print('域名{}解析失败........'.format(dns_name))
    return web_ip

def get_dns_from_ip138(ip_addr):
    '''
    从site.ip138.com去查找ip对应的域名
    https://site.ip138.com/192.126.127.240/
    :param ip_addr:
    :return: 域名列表
    '''
    dns_list = []
    host = 'site.ip138.com'
    url = 'https://site.ip138.com/{}/'.format(ip_addr)
    html_content = http_comm.https_get_html(url,  host)

    # 解析出域名
    start_index = html_content.find('<ul id="list">')
    end_index = html_content.find('</ul>', start_index)
    content = html_content[start_index:end_index]

    # 最多提取100个域名
    start_flag = 'target="_blank">'
    end_flag = '</a></li>'
    for i in range(0, 100):
        start_index = content.find(start_flag)
        if start_index <= 0:
            break

        end_index = content.find(end_flag, start_index)
        dns_name = content[start_index + len(start_flag):end_index]
        dns_list.append(dns_name)
        content = content[end_index + 1:]

    return dns_list


def get_dns_from_ip(ip_addr):
    '''
    查询出这个ip所关联的所有ip
    :param ip_addr:
    :return: 返回域名列表
    '''
    dns_list = get_dns_from_ip138(ip_addr)
    return dns_list

