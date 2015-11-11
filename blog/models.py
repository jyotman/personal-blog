from django.db import models
from django.utils import timezone
from django_markdown.models import MarkdownField


class Parking(models.Model):
    slot = models.IntegerField(default = -1)
    status = models.CharField(max_length = 7)

    def __str__(self):
        return self.status


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]