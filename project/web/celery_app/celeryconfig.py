# coding=utf-8

from datetime import timedelta
from celery.schedules import crontab

# 配置broker为redis
BROKER_URL = 'redis://localhost:6379/1'

# 配置结果存储至redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

# 时区设置
CELERY_TIMEZONE='Asia/Shanghai'

# 导入任务
CELERY_IMPORTS = (
    'celery_app.task'
    )

# 配置定时任务的调度器
CELERYBEAT_SCHEDULE={
    # 任务名字
    'test_task':{
        # 任务启动的函数
        'task':'celery_app.task.testf',
        # 定时时间设置，每10秒一次
        'schedule':timedelta(seconds=10),
        # 传递的参数
        'args':()
    },
    'crawler_task': {
        # 任务启动的函数
        'task': 'celery_app.task.crawler_task',
        # 定时时间设置，每10秒一次
        'schedule': timedelta(seconds=10),
        # 传递的参数
        'args': ()
    }
}