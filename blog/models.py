from django.db import models
from django.contrib.sitemaps import ping_google

class Parking(models.Model):
    slot = models.IntegerField(default = -1)
    status = models.CharField(max_length = 7)

    def __str__(self):
        return self.status

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

class Visit(models.Model):
    post = models.BooleanField()
    name = models.CharField(max_length=100)
    totalCount = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    dailyCount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)
    visits = models.ForeignKey(Visit)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

    def save(self, force_insert=False, force_update=False):
        super(Entry, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass