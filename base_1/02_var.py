# coding=utf-8
# python变量(变量使用、数字、  字符串、 字典、列表）
#
#

def int_var():
    '''
    整数相关的操作
    :return:
    '''
    print('---------------整数---------------')
    var_int = 10
    var_float = 10.0
    var_long = 51924361L
    var_complex = 3.14j
    print('var_int : {}'.format(var_int))
    print('var_float : {}'.format(var_float))
    print('var_long : {}'.format(var_long))
    print('var_complex : {}'.format(var_complex))
    print('-----整数加减乘除-----')
    print('1 + 2 = {}'.format(1 + 2))       #1  + 2 = 3
    print('3-1 = {}'.format(3 - 1))          # 3 - 1 = 2
    print('2*4 = {}'.format(2 * 4))          # 2 * 4 = 8
    print('6/3= {}'.format(6 / 3))           # 6 / 3 = 2
    print('\n\n')
    return

def str_var():
    '''
    字符串相关的操作
    :return:
    '''
    print('---------------字符串---------------')
    single_str = 'a'
    more_str = 'this is string'
    china_str = '中文字符串'
    print('单个字符 : {}'.format(single_str))
    print('字符串 : {}'.format(more_str))
    print('中文字符串 : {}'.format(china_str))

    print('-----字符串拼接-----')
    one_str = 'this'
    two_str = ' is good'
    end_str = one_str + two_str
    end1_str = '{}{}'.format(one_str, two_str)
    print('字符串相加 : ({})+({}) = ({})'.format(one_str, two_str, end_str))
    print('字符串格式化拼接 : ({})+({}) = ({})'.format(one_str, two_str, end1_str))

    print('-----字符串截取----')
    one_str = 'this is string'
    left_str = one_str[:4]      #:前不填为0， 取0~4个字符串(this)
    right_str = one_str[5:]   #:后不填为到最后，第5个字符串开始到结束(is string)
    middle_str = one_str[1:8] #:取第2到第9个(his is )
    print('({})截取左边4个字符串的结果为:{}'.format(one_str, left_str))
    print('({})截取从第5个字符串开始到结束字符串为:{}'.format(one_str, right_str))
    print('({})列表取第2到第9个变量作为子列表:({})'.format(one_str, middle_str))

    print('-----字符串查找、替换----')
    print('({})截取左边4个字符串的结果为:{}'.format(one_str, left_str))
    one_str = 'this is string'
    one_index = one_str.find('string')  #查找one_str字符串中string子串的开始位置
    print('({})字符串中查找string的位置为:{}'.format(one_str, one_index))

    one_str = 'this is string'
    dest_str = one_str.replace('string', 'man') #替换字符串中string为man，替换的结果为(this is man)
    print('({})字符串替换string为man的结果为:{}'.format(one_str, dest_str))
    print('\n\n')
    return

def list_var():
    '''
    列表相关的操作
    :return:
    '''
    print('---------------列表(list)---------------')
    one_list = []
    two_list = [1, 2, 3]
    three_list = ['a', 'b', 'this']
    four_list = [1, 2, 10.0, 'a', 'this']

    print('空列表 : {}'.format(one_list))
    print('数字列表 : {}'.format(two_list))
    print('字符串列表 : {}'.format(three_list))
    print('混合型变量列表 : {}'.format(four_list))

    print('-----list增加变量(append方法)----')
    one_list = [1, 2, 3]
    one_list.append('this')
    one_list.append(10)
    print('({}) append (this) (10) : {}'.format([1, 2, 3], one_list))

    print('-----list相加----')
    one_list = [1, 2, 3]
    two_list = ['a', 'b', 'this']
    end_list = one_list + two_list
    print('({})+({})=({})'.format(one_list, two_list, end_list))

    print('-----list变量获取----')
    one_list = [1, 2, 3]
    one_var = one_list[0]
    print('({})第一个变量为{}'.format(one_list, one_var))

    one_var = one_list.pop()
    print('({})pop第一个变量值{}, 当前列表为({})'.format( [1, 2, 3], one_var, one_list))

    print('-----list 字列表获取(string类似)----')
    one_list = [1, 2, 3, 4, 5, 6, 7, 8]
    left_list = one_list[:3]
    right_list = one_list[5:]
    middle_list = one_list[1:5]
    print('({})列表取前3个变量作为子列表:({})'.format(one_list, left_list))
    print('({})列表取从第6个变量到最后作为字列表:({})'.format(one_list, right_list))
    print('({})列表取第2到第6个变量作为子列表:({})'.format(one_list, middle_list))

    print('\n\n')
    return

def main():
    '''
    主函数
    :return:
    '''

    int_var()
    str_var()
    list_var()


    print('\n\n')


if __name__ == '__main__':
	main()
