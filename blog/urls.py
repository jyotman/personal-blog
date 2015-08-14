from django.conf.urls import url
from . import views

# from blog.views import ProfileImageIndexView, ProfileDetailView

from django.conf.urls.static import static
from django.conf import settings

from blog.views import ProfileImageView

urlpatterns = [
    url(r'^$', views.aboutme),
    # url(r'^$', views.post_list),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^parking/post/$', views.parkingUpdate),
    url(r'^parking/get/$', views.parkingAccess),
    url(r'^aboutme/$', views.aboutme),
    url(r'^contact/$', views.contact),

    url(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
]