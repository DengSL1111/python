# coding=utf-8
# python基本语法(判断逻辑)
#
#

import sys


def main():
    '''
    主函数
    :return:
    '''

    arg1 = int(sys.argv[1])

    if arg1 < 10:
        print('这是一个小于10的数字 : {}'.format(arg1))
    else:
        print('这是一个大于等于10的数字 : {}'.format(arg1))


    if arg1 < 10:
        print('这是一个小于10的数字 : {}'.format(arg1))
    elif (arg1 >= 10 and arg1 < 100):
        print('这是一个10~100之间的数字 : {}'.format(arg1))
    else:
        print('这是一个大于等于100的数字 : {}'.format(arg1))


    if arg1 < 10 or arg1 > 100:
        print('这是一个小于10或者大于100的数字 : {}'.format(arg1))

if __name__ == '__main__':
	main()
