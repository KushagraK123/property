# Generated by Django 2.2.6 on 2019-11-08 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_auto_20191107_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 8, 18, 29, 39, 768044)),
        ),
    ]
