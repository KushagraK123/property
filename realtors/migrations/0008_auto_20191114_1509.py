# Generated by Django 2.2.6 on 2019-11-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0007_merge_20191113_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='properties_sold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
