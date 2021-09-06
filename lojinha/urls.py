from django.conf.urls import url
from lojinha import views

urlpatterns = [
    url(r'^api/lojinha$', views.lojinha_list),
    url(r'^api/lojinha/(?P<pk>[0-9]+)$', views.lojinha_detalhada),
]
