from django.conf.urls import url
from .views import Index, Add

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Index, name='index-publicacion'),
    url(r'^add/$', Add, name='add-publicaciones'),
]