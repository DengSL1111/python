# coding=utf-8
# python基本语法(文件相关操作)
#
#
import ConfigParser


def file_write():
    '''
    写文件
    :return:
    '''

    # 创建一个文件并写入内容（如果文件存在，则覆盖）
    fp = open('test.txt', 'w')
    fp.write('this is python test file\n')
    fp.close()

    # 在文件末尾增加内容(文件不存在则创建)
    fp = open('test.txt', 'a')
    fp.write('append content\n')
    fp.close()
    print('创建文件test.txt并将内容写入\n')


def file_read():
    '''

    :return:
    '''
    print('读取test.txt文件内容')
    fp = open('test.txt', 'r')
    content = fp.read()
    fp.close()
    print('read test.txt file:{}'.format(content))

    print('逐行读取test.txt文件内容')
    line_index = 1
    fp = open('test.txt', 'r')
    while True:
        content = fp.readline()  # 只读取一行内容
        if not content:
            break

        print('第{}行:{}'.format(line_index, content))
        line_index += 1


def file_write_ini():
    '''
    写ini文件
    :return:
    '''
    config = ConfigParser.ConfigParser()
    config.add_section('weixin')
    config.set('weixin', 'user', 'test')
    config.set('weixin', 'passwd', '123456')
    config.write(open('user.ini', "w"))
    print('写入user.ini文件')

def file_read_ini():
    '''
    读取ini文件
    :return:
    '''
    deal_conf = ConfigParser.ConfigParser()
    deal_conf.read('/tmp/user.ini')
    username = deal_conf.get('weixin', 'user')
    passwd = deal_conf.get('weixin', 'passwd')
    print('user.ini 读取weixin节点 user:{}  passwd:{}'.format(username, passwd))


def main():
    '''
    主函数
    :return:
    '''

    file_write()
    file_read()

    file_write_ini()
    file_read_ini()




if __name__ == '__main__':
	main()
