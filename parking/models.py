from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Location(models.Model):
	user = models.ForeignKey(User)
	latitude = models.DecimalField(max_digits=10, decimal_places=10)
	longitude = models.DecimalField(max_digits=10, decimal_places=10)
	address = models.CharField(max_length=500)
	dateAdded = models.DateTimeField(auto_now_add=True)
	dateRetrieved = models.DateTimeField(auto_now=True)