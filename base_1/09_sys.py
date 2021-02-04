# coding=utf-8
# python基本语法(os sys系统库祥光操作)
#
#

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    '''
    主函数
    :return:
    '''

    os.system('pwd')

    path = '/tmp'
    print('{} is exists :{}'.format(path, os.path.exists(path)))
    print('{} is file :{}'.format(path, os.path.isfile(path)))
    print('{} is dir :{}'.format(path, os.path.isdir(path)))

    print('当前进程第1个参数:{}'.format(sys.argv[0]))
    print('当前运行平台操作系统 : {}'.format(sys.platform))

    #sys.exit(0)        #强制退出进程





if __name__ == '__main__':
	main()
