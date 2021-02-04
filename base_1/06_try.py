# coding=utf-8
# python基本语法(异常处理)
#
#

def test_except(test_var):
    '''
    测试异常变量
    :param test_var:
    :return:
    '''

    try:
        i_var = 1 + test_var
        a_var = 1 / test_var
    except TypeError as typ_ex:
        print('捕获到变量类型错误：{}'.format(typ_ex))
    except ZeroDivisionError as zero_ex:
        print('捕获到除法操作错误：{}'.format(zero_ex))
    finally:
        print('不管有没有异常，都到这里来')


def main():
    '''
    主函数
    :return:
    '''

    try:
        i_var = 1 +'string'
    except Exception as ex:
        print('捕获到异常：{}'.format(ex))

    try:
        i_var = 1/'string'
    except TypeError as ex:
        print('捕获到变量类型错误：{}'.format(ex))

    print('\n函数参数异常测试')
    test_except('string')
    test_except(0)
    test_except(2)





if __name__ == '__main__':
	main()
