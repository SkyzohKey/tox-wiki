from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.category, name='index'),
    url(r'^(?P<category>[^/]+)$', views.category, name='categories'),
    url(r'^(?P<category>[^/]+)/(?P<page_name>[^/]+)$', views.page, name='page')
]
