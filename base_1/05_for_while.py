# coding=utf-8
# python基本语法(循环逻辑)
#
#


def main():
    '''
    主函数
    :return:
    '''

    for i in range(0, 100):
        print('我是小明')

    i = 0
    while(i < 100):
        print('我是小明')
        i+=1

    sum = 0
    for i in range(1, 101):
        sum += i
    print('for : 1+2+...+100={}'.format(sum))

    sum = 0
    i = 0
    while(i <= 100):
        sum += i
        i+=1
    print('while : 1+2+...+100={}'.format(sum))

    #break
    for i in range(0, 100):
        print('this is {}'.format(i))
        if(i >= 2):
            break

    #continue
    for i in range(0, 100):
        if (i % 10 != 0):
            continue
        print('this is {}'.format(i))



if __name__ == '__main__':
	main()
