from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import StaticViewSitemap, BlogSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog' : BlogSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    	name='django.contrib.sitemaps.views.sitemap'),
    url(r'', include('blog.urls')),
]
