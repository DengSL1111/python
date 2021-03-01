from django.shortcuts import render
from django.views import generic
from testweb.models import CrawlerConf
from testweb.models import CrawlerRes


class IndexView(generic.ListView):
    '''

    '''

    template_name = 'testweb/crawler_list.html'
    context_object_name = 'crawler_list'

    def get_queryset(self):
        res = []

        crawler_list = CrawlerConf.objects.all()
        crawler_res_list = CrawlerRes.objects.all()

        for crawler_res in crawler_res_list:
            tmp_res = {}
            tmp_res['keyword'] = '-'
            keyword_info = crawler_list.filter(id=crawler_res.craw_id).first()
            if keyword_info:
                tmp_res['keyword'] = keyword_info.keyword

            tmp_res['host_ip'] = crawler_res.host_ip
            tmp_res['belong'] = crawler_res.belong
            tmp_res['main_dns'] = crawler_res.main_dns
            tmp_res['link_dns'] = crawler_res.link_dns[0:30]
            tmp_res['id'] = crawler_res.id
            res.append(tmp_res)

        return res
        #return CrawlerConf.objects.all()


