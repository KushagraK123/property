from django.db import models
from datetime import datetime
# Create your models here.


class Otp(models.Model):
    email = models.EmailField()
    otp = models.IntegerField()
    time = models.TimeField(blank=True)
