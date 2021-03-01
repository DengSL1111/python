from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import CrawlerConf


class CrawlerConfAdmin(admin.ModelAdmin):
    '''

    '''

    list_display = ('keyword', 'start_page', 'end_page', 'detail')

    # 配置查询字段
    search_fields = ('keyword',)
    # 配置排序
    ordering = ('id',)

    # 配置在新增，编辑页面中显示的字段
    fields = ('keyword', 'start_page', 'end_page')

    #=======
    def detail(self, obj):
        #return '<a href="%s%s">%s</a>' % ('http://url-to-prepend.com/', obj.url_field, obj.url_field)
        detail_html = u'<a href="/crawler/{}">详情</a>'.format(obj.id)
        return format_html(detail_html)

    #<a href="/admin/testweb/crawlerconf/1/change/">我的世界</a>
    #<td class="field-detail">&lt;a href="/admin/testweb/crawlerconf/1/change/"&gt;详情&lt;/a&gt;</td>
    #<th class="field-keyword"><a href="/admin/testweb/crawlerconf/1/change/">我的世界</a></th>

    detail.allow_tags = True
    detail.short_description = 'detail'


admin.site.register(CrawlerConf, CrawlerConfAdmin)
