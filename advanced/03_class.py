# coding=utf-8
# 类（面向对象）


class  Animal():
    '''
    定义一个动物类
    '''

    def __init__(self, weight):
        '''
        Animal初始化函数
        :param weight:
        '''

        self.weight = weight
        print('我是一个Animal，我的体重是：{}'.format(self.weight))


    def action(self):
        '''
        动作
        :return:
        '''
        print('我是Aminal, 我会走路')

    def animal_func(self):
        '''
        animal 成员变量、成员方法调用测试
        :return:
        '''
        self.__private_animal_func()

    def __private_animal_func(self):
        '''
        私有化函数
        :return:
        '''
        print('__private_animal_func 是一个私有化函数，只能在类内部调用')


class Dog(Animal):
    '''
    定义一个类（狗）（继承自动物类Animal）
    '''

    def __init__(self, weight):
        '''
        Dog类初始化函数
        :param weight:
        '''
        Animal.__init__(self, weight)


class Bird(Animal):
    '''
    定义一个类（鸟）（继承自动物类Animal）
    '''

    def __init__(self, weight):
        '''
        Bird类初始化函数
        :param weight:
        '''
        Animal.__init__(self, weight)
        self. flight_speed = 50

    def action(self):
        '''
        动作
        :return:
        '''
        print('我是Bird, 我会飞')

    def action1(self):
        '''
        动作
        :return:
        '''
        print('我是Bird, 我还有一个动作是俯冲，速度为每分钟{}米'.format(self.flight_speed))


def main():
    '''
    主函数
    :return:
    '''

    animal = Animal(weight=10)
    animal.action()
    # animal.animal_func()
    # #animal.__private_animal_func()
    # print('main函数中animal.weight = {}'.format(animal.weight))

    print('')
    dog = Dog(weight=20)
    dog.action()

    print('')
    bird = Bird(weight=30)
    bird.action()
    bird.action1()

if __name__ == '__main__':
	main()
