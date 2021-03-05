from django.db import models
# Create your models here.


class CrawlerConf(models.Model):
    '''
    爬虫配置表
    '''
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    keyword = models.CharField(max_length=255, unique=True)
    start_page = models.IntegerField()
    end_page = models.IntegerField()
    extra = models.TextField(null=True)

    # def __str__(self):
    #     return self.id

    class Meta:
        verbose_name = u'关键字管理'
        verbose_name_plural = u'关键字管理'
        # app_label = u'关键字管理'


class CrawlerRes(models.Model):
    '''
    结果表
    '''
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    craw_id = models.IntegerField()
    host_ip = models.CharField(max_length=255)
    belong = models.CharField(max_length=255)
    main_dns = models.CharField(max_length=255)
    link_dns = models.TextField(null=True)
    extra = models.TextField(null=True)

    def __str__(self):
        return self.id


class OprLog(models.Model):
    '''
    操作日志
    '''
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    status = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    extra = models.TextField(null=True)
