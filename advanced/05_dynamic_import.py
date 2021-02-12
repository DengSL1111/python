# coding=utf-8
# 动态导入模块

import importlib

def main():
    '''
    主函数
    :return:
    '''

    param_check =importlib.import_module('common.param_check')
    try:
        param_check.check_int(10)
        param_check.check_int('aaaa')
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
	main()
