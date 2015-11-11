from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^parking/post/$', views.parkingUpdate),
    url(r'^parking/get/$', views.parkingAccess),
    url(r'^aboutme/$', views.aboutme),
    url(r'^contact/$', views.contact),
]