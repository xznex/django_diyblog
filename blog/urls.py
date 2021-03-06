from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bloggers/$', views.AuthorsList.as_view(), name='bloggers'),
    url(r'^blogger/(?P<pk>\d+)$', views.AuthorDetail.as_view(), name='author'),
    url(r'^blogs/$', views.BlogsList.as_view(), name='blogs'),
    url(r'^post/(?P<pk>\d+)$', views.BlogDetail.as_view(), name='blog'),
    url(r'^(?P<pk>\d+)/create$', views.CreateComment.as_view(), name='create_comment')
]
