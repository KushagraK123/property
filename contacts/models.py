from django.db import models
from datetime import datetime


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    seen = models.BooleanField(default=False)
    realtor_reply = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name


