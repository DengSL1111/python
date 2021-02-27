from django.conf.urls import  url
from testweb import views

# urlpatterns = patterns('',
#     url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='cms-story'),
#     url(r'^$', views.IndexView.as_view(), name='crawler-home'),
#     )
    
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='crawler-home'),
    url(r'^$', views.CrawlerAddView.as_view(), name='crawler-add'),
    url(r'^$', views.SearchView.as_view(), name='crawler-search'),

]