# Generated by Django 3.2 on 2021-08-09 08:11

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('jewlery', '0005_auto_20210808_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitmodel',
            name='jdatetime',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 8, 9, 12, 40, 44, 794974)),
        ),
    ]
