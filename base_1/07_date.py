# coding=utf-8
# python基本语法(时间相关函数)
#
#
import time
import datetime


def time_func():
    ''''
    '''

    print('----------time----------')
    cur_time = time.time()
    print('当前时间戳 : {}'.format(cur_time))

    localtime = time.localtime()
    print('本地时间 : {}'.format(localtime))
    print('本地时间 : {}-{}-{} {}:{}:{}'.format(localtime.tm_year,
                                            localtime.tm_mon,
                                            localtime.tm_mday,
                                            localtime.tm_hour,
                                            localtime.tm_min,
                                            localtime.tm_sec))
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
    print('本地时间 : {}'.format(str_time))

    print('time.sleep 休眠3秒')
    time.sleep(3)
    print('休眠3秒结束')

    print('\n----------datetime----------')
    today = datetime.date.today()
    print('今天是 : {}'.format(today))

    cur_dt = datetime.datetime.now()
    str_dt = datetime.datetime.strftime(cur_dt, '%Y-%m-%d %H:%M:%S')
    print('现在是(时间对象) : {}'.format(cur_dt))
    print('现在是(时间字符串) : {}'.format(str_dt))

    str_p = '2019-01-30 10:10:10'
    date_p = datetime.datetime.strptime(str_p, '%Y-%m-%d %H:%M:%S')
    print('时间字符串({})转成时间对象为:{}'.format(str_p, date_p))

    today = datetime.datetime.now()
    pre_hour = today + datetime.timedelta(hours=-1)
    next_hourt = today + datetime.timedelta(hours=1)
    yestoday = today + datetime.timedelta(days=-1)
    tomorrow = today + datetime.timedelta(days=1)
    print('现在是 : {}'.format(today))
    print('现在的前一个小时是 : {}'.format(pre_hour))
    print('现在的后一个小时是 : {}'.format(next_hourt))
    print('昨天的现在是 : {}'.format(yestoday))
    print('明天的现在是 : {}'.format(tomorrow))


def main():
    '''
    主函数
    :return:
    '''

    time_func()




if __name__ == '__main__':
	main()
