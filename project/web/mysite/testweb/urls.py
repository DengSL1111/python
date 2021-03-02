from django.conf.urls import  url
from testweb import views

    
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='crawler-home'),
    url(r'^detail/$', views.DetailView.as_view(), name='crawler_detail'),
]