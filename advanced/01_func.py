# coding=utf-8
# 函数

import time


def test_func():
    '''
    这是一个测试函数
    :return:
    '''
    print('这是一个测试函数')
    return

def save_cur_time():
    '''
    保存当前时间
    :return:
    '''
    localtime = time.localtime()
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", localtime)

    fp = open('cur_time.txt', 'a+')
    fp.write(str_time)
    fp.write('\r\n')
    fp.close()

def save_file(filename, content):
    '''
    将内容保存到文件中
    :param filename: 文件名
    :param content: 要保存的内容
    :return:
    '''
    fp = open(filename, 'a+')
    fp.write(content)
    fp.close()

def immutable_param(param):
    '''
    不可变类型参数函数
    :param param: 参数值 (int)
    :return:
    '''
    print('immutable_param param传入值为 : {}'.format(param))
    param = 10
    print('immutable_param param修改后的值为 : {}'.format(param))


def mutable_param(param):
    '''
    可变类型参数函数
    :param param: 参数值 (dict)
    :return:
    '''
    print('mutable_param param传入值为 : {}'.format(param))
    del param['1key']
    param['10key'] = '10value'
    print('mutable_param param修改后的值为 : {}'.format(param))


def default_param(param1, param2 = 10):
    '''
    默认参数函数
    :param param1: 参数1
    :param param2: 默认参数，默认值为10
    :return:
    '''

    print('default_param param1:{}  param2:{}'.format(param1, param2))


def variable_param(param1, *kwarg):
    '''
    可变参数函数
    :param param1: 参数1
    :param kwarg:  可变参数
    :return:
    '''

    print('variable_param param1:{}'.format(param1))
    for var in kwarg:
        print('variable_param kwarg:{}'.format(var))


def add(a, b):
    '''
    计算a+b的结果
    :param a:  参数a(int）
    :param b: 参数b（int)
    :return:  int
    '''

    sum = a + b
    return sum


def main():
    '''
    主函数
    :return:
    '''
    save_cur_time()

    param = 1
    immutable_param(param)
    print('函数结束后，param的值为: {}'.format(param))
    print('\n')

    param = {'1key': '1value', '2key': '2value'}
    mutable_param(param)
    print('函数结束后，param的值为: {}'.format(param))
    print('\n')

    default_param(1, 2)
    default_param(1)
    print('\n')

    variable_param(10, 20,  30)
    variable_param(10, 20, 30, 40, 50)
    print('\n')

    sum = add(1, 2)
    print('add(1, 2)的返回值为: {}'.format(sum))
    print('\n')


if __name__ == '__main__':
	main()
