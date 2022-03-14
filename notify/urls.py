from django.urls import path, include, re_path
from .views import notifyPubViewSetList, notifyViewSetList


urlpatterns = [
    re_path(r'^notify/create/$', notifyPubViewSetList.as_view({'post': 'create'})),
    re_path(r'^notify/send/(?P<pk>\d+)/$', notifyPubViewSetList.as_view({'get': 'retrieve'})),
    re_path(r'^notify/receive/(?P<pk>\d+)/$', notifyViewSetList.as_view({'get': 'retrieve'})),
]