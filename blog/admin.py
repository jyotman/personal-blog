from django.contrib import admin
from .models import Entry, Parking, Tag, Visit
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

class EntryAdmin(MarkdownModelAdmin):
	list_display = ("title", "created")
	prepopulated_fields = {"slug" : ("title",)}
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class VisitAdmin(admin.ModelAdmin):
	list_display = ('name', 'date', 'dailyCount')

admin.site.register(Entry, EntryAdmin)

admin.site.register(Parking)
admin.site.register(Tag)
admin.site.register(Visit, VisitAdmin)