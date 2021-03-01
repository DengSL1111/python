from django.conf.urls import  url
from testweb import views

# urlpatterns = patterns('',
#     url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='cms-story'),
#     url(r'^$', views.IndexView.as_view(), name='crawler-home'),
#     )
    
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='crawler-home'),
]