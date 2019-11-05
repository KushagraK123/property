# Generated by Django 2.2.6 on 2019-10-26 13:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=10)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%M/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%M/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%M/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%M/%d')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%M/%d')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%M/%d')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%M/%d')),
                ('isPublished', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 26, 13, 27, 52, 201318))),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]
