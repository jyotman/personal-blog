from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'', include('blog.urls')),
    url(r'', include('parking.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
