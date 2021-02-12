# coding=utf-8
# 模块

from common import param_check
from common import ip_check

def main():
    '''
    主函数
    :return:
    '''


    try:
        param_check.check_int(10)
        param_check.check_int('aaaa')
    except Exception as ex:
        print(ex)

    try:
        ip_check.ipv4_check('192.168.10.1')
        ip_check.ipv4_check('1111.11.11.1')
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
	main()
