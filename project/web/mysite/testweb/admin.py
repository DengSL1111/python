from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import CrawlerConf


class CrawlerConfAdmin(admin.ModelAdmin):
    '''
    关键字配置页面注册
    '''

    # 页面显示的字段
    list_display = ('keyword', 'start_page', 'end_page', 'detail')

    # 配置查询字段
    search_fields = ('keyword',)

    # 配置排序
    ordering = ('id',)

    # 配置在新增，编辑页面中显示的字段
    fields = ('keyword', 'start_page', 'end_page')

    def detail(self, obj):
        #return '<a href="%s%s">%s</a>' % ('http://url-to-prepend.com/', obj.url_field, obj.url_field)
        detail_html = u'<a href="/crawler/">详情</a>'
        return format_html(detail_html)

    detail.allow_tags = True
    detail.short_description = 'detail'


admin.site.register(CrawlerConf, CrawlerConfAdmin)
