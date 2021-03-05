# coding=utf-8
# Copyright Sangfor. All rights reserved

import MySQLdb
from celery_app.crawler  import info_ini
from celery_app.crawler  import comm

class  SqlOpr():
    '''
    数据库操作类
    '''

    def __init__(self,):
        '''
        初始化函数
        '''

        sql_ip = 'localhost'
        sql_user = 'root'
        sql_pwd = '123456'
        sql_db = 'mysite'
        self.db = MySQLdb.connect(sql_ip, sql_user, sql_pwd, sql_db, charset='utf8')
        self.cursor = self.db.cursor()

    def __del__(self):
        '''
        析构函数
        :return:
        '''

        self.cursor.close()
        self.db.close()

    def query(self, sql):
        '''
        执行sql语句
        :param sql:
        :return:
        '''

        res = []
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                res.append(list(row))

            return res
        except:
            print('query sql failed: {}'.format(sql))

    def exec(self, sql):
        '''
        执行删除更新的sql操作
        :param sql:
        :return:
        '''
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

def get_all_keywords():
    '''
    获取所有的关键字信息
    :return:
    '''
    tablename = 'testweb_crawlerconf'
    sql = 'select * from {}'.format(tablename)

    sql_obj = SqlOpr()
    keywords_list = sql_obj.query(sql)

    info_obj = info_ini.InfoIniObj()
    for keywors in keywords_list:
        key_obj = info_ini.KeyIniObj()
        key_obj.craw_id = keywors[0]
        key_obj.keyword = keywors[1]
        key_obj.start_page = keywors[2]
        key_obj.end_page = keywors[3]
        info_obj.key_list.append(key_obj)

    return info_obj


def del_crawler_res(craw_id):
    '''
    删除某个关键字的所有结果
    :param craw_id:
    :return:
    '''

    tablename = 'testweb_crawlerres'
    sql = 'delete from {} where craw_id = {}'.format(tablename, craw_id)
    sql_obj = SqlOpr()
    sql_obj.exec(sql)


def add_crawler_res(crawler_res, craw_id):
    '''
    批量新增关键字结果
    :param crawler_res_list:
    :return:
    '''

    tablename = 'testweb_crawlerres'
    sql_obj = SqlOpr()
    for web_ip, host_info in crawler_res.items():
        belong = host_info.get('belong')
        main_dns = ','.join(comm.dictkey_to_list(host_info['dns_info']))

        #关联域名
        link_dns_dict = {}
        for dns_name, dns_info in host_info['dns_info'].items():
            for tmp_dns_name in dns_info['link_dns']:
                link_dns_dict[tmp_dns_name] = {}

        link_dns = ','.join(comm.dictkey_to_list(link_dns_dict))

        sql = 'insert into {}(craw_id,host_ip,belong,main_dns,link_dns,extra) \
        values({},"{}","{}","{}","{}","{}")'.format(tablename,
                                                                 craw_id, web_ip, belong,
                                                                 main_dns, link_dns, '')
        #print(sql)
        sql_obj.exec(sql)


if __name__ == '__main__':
    get_all_keywords()

