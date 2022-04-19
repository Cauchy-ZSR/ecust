from django.urls import re_path
from .views import topicDetailViewSet, topicViewSetList, forumDetailViewSetList, forumViewSetList, commentViewSet, commentDetailViewSet, membershipViewSet, commentIsReadViewSet


urlpatterns = [
    re_path(r'^forum/$', forumDetailViewSetList.as_view({'get': 'list'})),
    re_path(r'^forum/(?P<pk>\d+)/$', forumViewSetList.as_view({'get': 'retrieve'})),
    re_path(r'^forum/create/$', forumViewSetList.as_view({'post': 'create'})),
    re_path(r'^forum/update/(?P<pk>\d+)/$', forumViewSetList.as_view({'put': 'update'})),
    re_path(r'^topic/create/$', topicViewSetList.as_view({'post': 'create'})),
    re_path(r'^topiclist/(?P<pk>\d+)', topicDetailViewSet.as_view({'get': 'list'})),
    re_path(r'^topic/(?P<pk>\d+)/$', topicDetailViewSet.as_view({'get': 'retrieve'})),
    re_path(r'^commentlist/(?P<pk>\d+)/$', commentDetailViewSet.as_view({'get': 'list'})),
    re_path(r'^comment/create/$', commentViewSet.as_view({'post': 'create'})),
    re_path(r'^comment/delete/(?P<pk>\d+)', commentViewSet.as_view({'delete': 'delete'})),
    re_path(r'^comment/is_read/(?P<pk>\d+)', commentDetailViewSet.as_view({'get': 'retrieve'})),
    re_path(r'^comment/detail/is_read/(?P<pk>\d+)', commentIsReadViewSet.as_view({'get': 'list'})),
    re_path(r'^comment/is_read/update/(?P<pk>\d+)', commentIsReadViewSet.as_view({'post': 'retrieve'})),
    re_path(r'^membership/check/$', membershipViewSet.as_view({'post': 'retrieve'})),
    re_path(r'^membership/create/$', membershipViewSet.as_view({'post': 'create'})),
    re_path(r'^membership/delete/$', membershipViewSet.as_view({'delete': 'delete'})),
]