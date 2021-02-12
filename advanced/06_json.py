# coding=utf-8
# json格式

import json

def main():
    '''
    主函数
    :return:
    '''

    dict_data = {'key1': 'value1'}
    print('dict_data : {}'.format(dict_data))

    json_data = json.dumps(dict_data)
    print('dict to json : {}'.format(json_data))

    dict_data = json.loads(json_data)
    print('json to dict : {}'.format(dict_data))


if __name__ == '__main__':
	main()
