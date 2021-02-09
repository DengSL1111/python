# coding=utf-8
# 装饰器


def func_obj():
    '''
    函数对象测试函数
    :return:
    '''

    print('这是一个函数')

def internal_func():
    '''
    子函数示例函数
    :return:
    '''

    print('子函数示例')

    def hello():
        print('this is hello function')

    def test():
        print('this is test funcion')

    hello()

def func_param_func(func_param):
    '''
    执行func_param对应的参数
    :param func_param: 函数对象
    :return:
    '''

    print('执行{}函数'.format(func_param))
    func_param()

def func_trace(func):
    '''
    装饰器函数，用于func函数名
    :param func: 函数对象
    :return:
    '''

    def wrapper(*args, **kwargs):
        print('[func_trace]: enter {}()'.format(func.__name__))
        return func(*args, **kwargs)

    return wrapper

@func_trace
def add_func(a, b):
    '''
    整数相加
    :param a:
    :param b:
    :return:
    '''

    sum = a + b
    return sum


class Decorate(object):
    '''

    '''
    def __init__(self):
        '''
        初始化
        '''
        print('Decorate init')

    def __call__(self,  func):
        '''

        :param func:
        :return:
        '''
        def wrapper(*args, **kwargs):
            print('[Decorate]: enter {}()'.format(func.__name__))
            return func(*args, **kwargs)

        return wrapper


@Decorate()
def sub_func(a, b):
    '''
    a - b
    :param a:
    :param b:
    :return:
    '''
    return a - b


def main():
    '''
    主函数
    :return:
    '''

    print('func_obj函数对象: {}'.format(func_obj))

    func_obj()
    func_test = func_obj
    func_test()

    internal_func()

    func_param_func(func_obj)

    sum = add_func(1, 2)
    print('add_func(1, 2) = {}'.format(sum))

    sum = sub_func(10, 2)
    print('sub_func(10, 2) = {}'.format(sum))

if __name__ == '__main__':
	main()
