# coding=utf-8
# 参数校验（公共模块）

from param_exception import ParamException

def check_int(i_param):
    '''
    校验i_param参数是否为int，不是则抛出异常
    :param i_param:
    :return:
    '''

    if not isinstance(i_param, int):
        raise ParamException('参数{}必须为一个int类型'.format(i_param))


def check_str(str_param):
    '''
    校验参数是否为str，不是则抛出异常
    :param str_param:
    :return:
    '''

    if not isinstance(str_param, str):
        raise ParamException('参数{}必须为一个字符串类型'.format(str_param))

    if not str_param:
        raise  ParamException('参数不能为空')