from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<category>[\w-]+)/(?P<page_name>[\w-]+)$', views.page, name='page')
]
