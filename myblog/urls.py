from django.conf.urls import url
from . import views
from myblog.feeds import AllPostsRssFeed

app_name = 'myblog'
#视图函数命名空间，标识该urls属于myblog应用
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),
    # 该URL完成两个功能：1，将URL和视图函数进行绑定。2，当调用视图函数时，会将(?P<pk>[0-9]+)中pk所匹配的值传入detail
    #相当于 detail （request，pk=pk）
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivesView.as_view(),name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>[0-9])/$',views.TagView.as_view(),name='tag'),
    url(r'^search/$',views.search,name='search'),
    url(r'^all/rss/$',AllPostsRssFeed(),name='rss'),
]