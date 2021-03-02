from django.shortcuts import render
from django.views import generic
from testweb.models import CrawlerConf
from testweb.models import CrawlerRes

import json

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
            if len(crawler_res.link_dns) < 30:
                tmp_res['link_dns'] = crawler_res.link_dns
            else:
                tmp_res['link_dns'] = crawler_res.link_dns[0:30] + '......'
            tmp_res['id'] = crawler_res.id
            res.append(tmp_res)

        return res
        #return CrawlerConf.objects.all()


class DetailView(generic.ListView):
    '''

    '''

    template_name = 'testweb/crawler_detail.html'
    context_object_name = 'crawler_detail'

    def get_queryset(self):
        res = {'keyword': '-', }

        params = self.request.GET.dict()
        crawler_res_id = params.get('crawler_id')
        if crawler_res_id:
            crawler_res = CrawlerRes.objects.filter(id=crawler_res_id).first()
            if crawler_res:
                keyword_info = CrawlerConf.objects.filter(id=crawler_res.craw_id).first()
                if keyword_info:
                    res['keyword'] = keyword_info.keyword

                res['host_ip'] = crawler_res.host_ip
                res['belong'] = crawler_res.belong
                res['main_dns'] = crawler_res.main_dns
                res['link_dns'] = crawler_res.link_dns

        return res
