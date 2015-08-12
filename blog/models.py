from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Parking(models.Model):
    slot = models.IntegerField(default = -1)
    status = models.CharField(max_length = 7)

    def __str__(self):
        return self.status

class ProfileImage(models.Model):
    image = models.FileField(upload_to='profile/%Y/%m/%d')

