# coding=utf-8
# python基本语法(系统包导入)
#
#

import os
import time


def main():
    '''
    主函数
    :return:
    '''

    os.system('ls -al')     #执行linux命令ls -al，列出当前目录下的所有文件
    os.system('touch /tmp/aa.txt')  #执行系统命令 touch /tmp/aa.txt， 创建一个文件/tmp/aa.txt
    print(os.path.exists('/tmp/aa.txt'))    #判断文件/tmp/aa.txt是否存在

    cur_time = int(time.time())
    print('当前系统时间戳:{}'.format(int(cur_time)))


if __name__ == '__main__':
	main()
