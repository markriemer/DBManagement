
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pub/$', views.pubshell, name='pubshell'),
    url(r'^publishers/$', views.publishers, name='publishers'),
    url(r'^publishers/addpub$', views.addpub, name='addpublishers'),
    url(r'^publishers/orderby/(?P<orderby>-?pub\_id|-?name)$', views.publishers, name='sortedpublishers'),
    url(r'^publishers/deletepub/(?P<pub_id>[0-9]+)$', views.deletepub, name='deletepub'),
    url(r'^publishers/updatepub/(?P<pub_id>[0-9]+)$', views.updatepub, name='updatepub'),
    url(r'^auth/$', views.authshell, name='authshell'),
    url(r'^authors/$', views.authors, name='authors'),
    url(r'^authors/addauth$', views.addauth, name='addauthors'),
    url(r'^authors/orderby/(?P<orderby>-?auth\_id|-?name)$', views.authors, name='sortedauthors'),
    url(r'^authors/deleteauth/(?P<auth_id>[0-9]+)$', views.deleteauth, name='deleteauth'),
    url(r'^authors/updateauth/(?P<auth_id>[0-9]+)$', views.updateauth, name='updateauth'),
    url(r'^book/(?P<book_id>[0-9]+)$', views.updatebook, name='updatebook'),
    url(r'^book/modify/(?P<book_id>[0-9]+)$', views.modifybook, name='modifybook'),
    url(r'^book/modify/(?P<book_id>-1)$', views.modifybook, name='modifybook'),
    url(r'^book/unlink/(?P<wrote_id>[0-9]+)$', views.unlink, name='unlink'),
    url(r'^book/link$', views.link, name='link'),
    url(r'^book/deletebook/(?P<book_id>[0-9]+)$', views.deletebook, name='deletebook'),
    url(r'^book/add/$', views.addbook, name='addbook'),
]
