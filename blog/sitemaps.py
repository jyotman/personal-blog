from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from .models import Entry

class BlogSitemap(sitemaps.Sitemap):
	changefreq = "never"
	priority = 0.5

	def items(self):
		return Entry.objects.all()

	def lastmod(self, obj):
		return obj.modified

	def location(self, item):
		return '/entry/'+ str(item.slug)

class StaticViewSitemap(sitemaps.Sitemap):
	priority = 0.5
	changefreq = 'daily'

	def items(self):
		return ['index', 'aboutme', 'contact', 'privacypolicy', 'terms']

	def location(self, item):
		return reverse(item)