from django.conf.urls import url
from . import views





urlpatterns = [
    url(r'^$', views.friend_list, name='friend_list'),
    url(r'^friend/(?P<pk>\d+)/$', views.friend_detail, name='friend_detail'),
    url(r'^friend/(?P<pk>\d+)/edit/$', views.friend_edit, name='friend_edit'),
    url(r'^friend/(?P<pk>\d+)/approve/$', views.friend_approve, name='friend_approve'),
    url(r'^friend/(?P<pk>\d+)/remove/$', views.friend_remove, name='friend_remove'),
    url(r'^friend/new/$', views.friend_new, name='friend_new'),
    url(r'^friend/drafts/$', views.friend_draft_list, name='friend_draft_list'),
    url(r'^friend/(?P<pk>\d+)/memo/$', views.add_memo_to_friend, name='add_memo_to_friend'),
]
