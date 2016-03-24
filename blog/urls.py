from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^aboutme/$', views.aboutme, name="aboutme"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^privacypolicy/$', views.privacyPolicy, name="privacypolicy"),
    url(r'^terms/$', views.terms, name="terms"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^tag/(?P<slug>\S+)$', views.BlogIndexTag.as_view(), name="index_tag"),
    url(r'^parking/post/$', views.parkingUpdate),
    url(r'^parking/get/$', views.parkingAccess),

    #For google wenmaster verification
    url(r'^googlef70e42b57a682b5c\.html/$', views.webmasterVerify, name="verify"),
]