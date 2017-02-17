from django.conf.urls import url
from .api_views import UserList, UserDetail, PublicacionList

urlpatterns = [
    url(r'^$', UserList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^publicacionesapi/$', PublicacionList.as_view()),
]