from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(decimal_places=1, max_digits=10)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%y/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    isPublished = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
