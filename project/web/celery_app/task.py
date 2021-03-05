# coding=utf-8

import time
from celery_app import app
from celery_app.crawler import crawler

@app.task
def testf():
    '''
    :return:
    '''
    print('test crawler funcion')


@app.task
def crawler_task():
    '''
    :return:
    '''
    #读取配置
    crawler.crawler_main()