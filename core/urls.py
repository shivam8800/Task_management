from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name="home"),
    url(r'^project_page/(?P<pk>\d+)/$',views.detail, name="detail"),
    url(r'^task_page/(?P<pk>\d+)/$', views.comment, name="comment"),
    url(r'^postnestedcomment/$', views.nestedcomment, name="nestedcomment"),
    url(r'^assign_task/(?P<pk>\d+)/$', views.assign_task, name="assign_task"),
]