# coding=utf-8
# 爬虫

from celery_app.crawler import  const
from celery_app.crawler import info_ini
from celery_app.crawler import baidu_wd_dns
from celery_app.crawler import dns_ip
from celery_app.crawler import comm
# from celery_app.crawler .sql_opr import SqlOpr
from celery_app.crawler  import sql_opr


def get_dns_detail(dns_list):
    '''

    :param dns_list:
    :return:
    '''
    dns_detail_info = {}
    cur_index = 0
    total = len(dns_list)
    for dns_name in dns_list:
        cur_index += 1
        web_ip = dns_ip.get_dns_ip(dns_name)
        if not web_ip:
            continue

        if web_ip not in dns_detail_info.keys():
            dns_detail_info[web_ip] = {}
            dns_detail_info[web_ip]['dns_info'] = {}
            dns_detail_info[web_ip]['belong'] = dns_ip.get_ip_belong(web_ip)

            dns_detail_info[web_ip]['dns_info'][dns_name] = {}
            dns_detail_info[web_ip]['dns_info'][dns_name]['link_dns'] = \
                dns_ip.get_dns_from_ip(web_ip)

        comm.log_print("域名解析({}/{}) ： {}对应的ip地址为: {}".format(
            cur_index, total, dns_name, web_ip))

    return dns_detail_info


def crawler_main():
    '''
    主函数
    :return:
    '''

    info_obj = sql_opr.get_all_keywords()
    baidu_wd_dns.get_baidu_keyword_dns(info_obj.key_list)

    for key_obj in info_obj.key_list:
        dns_detail_info = get_dns_detail(key_obj.dns_list)
        sql_opr.del_crawler_res(key_obj.craw_id)
        sql_opr.add_crawler_res(dns_detail_info, key_obj.craw_id)


