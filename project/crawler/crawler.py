# coding=utf-8
# 爬虫

import const
import info_ini
import baidu_wd_dns
import dns_ip
import comm

def main():
    '''
    主函数
    :return:
    '''

    info_obj = info_ini.read_info_ini()
    dns_list = baidu_wd_dns.get_baidu_keyword_dns(info_obj.key_list)

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

    comm.save_collect_info(const.COLLECT_INFO_FILE, dns_detail_info)

if __name__ == '__main__':
	main()
