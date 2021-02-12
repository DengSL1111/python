# coding=utf-8
# ip校验模块（公共模块）

from param_exception import ParamException

def ipv4_check(ip_str):
    '''
    ipv4格式校验，错误抛出异常
    :param ip_str: ipv4字符串，如192.168.1.1
    :return:
    '''

    sep_list = ip_str.split('.')
    if len(sep_list) != 4:
        raise ParamException('ip({})错误，请传入ipv4参数(192.168.1.1)'.format(ip_str))

    for sep in sep_list:
        try:
            int_sep = int(sep)
            if int_sep < 0 or int_sep > 255:
                raise ParamException('ip({})错误，请传入ipv4参数(192.168.1.1)'.format(ip_str))
        except ValueError, e:
            raise ParamException('ip({})错误，请传入ipv4参数(192.168.1.1)'.format(ip_str))
