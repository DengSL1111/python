from django.shortcuts import render
from django.views import generic
from testweb.models import CrawlerConf

class IndexView(generic.ListView):
    '''

    '''

    template_name = 'testweb/crawler_list.html'
    context_object_name = 'crawler_list'
    def get_queryset(self):
        return CrawlerConf.objects.all()


class CrawlerAddView(generic.ListView):
    '''

    '''

    template_name = 'testweb/crawler_list.html'
    context_object_name = 'crawler_list'
    def get_queryset(self):
        return CrawlerConf.objects.all()




class SearchView(generic.ListView):
    '''

    '''

    template_name = 'testweb/crawler_list.html'
    context_object_name = 'crawler_list'
    def get_queryset(self):
        return CrawlerConf.objects.all()
