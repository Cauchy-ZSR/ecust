from django.urls import re_path
from .views import userDetailViewSetList, userViewSetList



urlpatterns = [
    re_path(r'^user/$', userDetailViewSetList.as_view({'get':'list'})),
    re_path(r'^user/retrieve/(?P<pk>\w+)/$', userDetailViewSetList.as_view({'get':'retrieve'})),
    re_path(r'^user/create/$', userViewSetList.as_view({'post':'create'})),
    re_path(r'^user/login/(?P<pk>\d+)/$', userViewSetList.as_view({'get': 'retrieve'})),
    re_path(r'^user/update/(?P<pk>\d+)/$', userViewSetList.as_view({'put': 'update'}))
]