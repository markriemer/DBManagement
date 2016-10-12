
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^publishers/$', views.publishers, name='publishers'),
    url(r'^publishers/orderby/(?P<orderby>-?pub\_id|-?name)$', views.publishers, name='sortedpublishers'),
    url(r'^publishers/deletepub/(?P<pub_id>[0-9]+)$', views.deletepub, name='deletepub'),
    url(r'^publishers/updatepub/(?P<pub_id>[0-9]+)$', views.updatepub, name='updatepub'),
]
