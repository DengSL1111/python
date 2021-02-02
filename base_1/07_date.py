# coding=utf-8
# python基本语法(时间相关函数)
#
#
import time
import datetime









def time_func():
    ''''
    '''

    cur_time = time.time()
    print('当前时间戳 : {}'.format(cur_time))

    localtime = time.localtime()
    print('本地时间 : {}'.format(localtime))
    print('本地时间 : {}-{}-{} {}:{}:{}'.format(localtime.tm_year, localtime.tm_mon, localtime.tm_mday,
                                          localtime.tm_hour, localtime.tm_min, localtime.tm_sec))
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    print('本地时间 : {}'.format(str_time))

    print('time.sleep 休眠3秒')
    time.sleep(2)
    print('休眠3秒结束')

    today = datetime.date.today()
    print('today is : {}'.format(today))




def main():
    '''
    主函数
    :return:
    '''

    time_func()




if __name__ == '__main__':
	main()
