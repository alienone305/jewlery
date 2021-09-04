# Generated by Django 3.2 on 2021-08-07 15:05

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('jewlery', '0003_jewlerymodel_is_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('datetime', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 8, 7, 19, 35, 29, 722621))),
            ],
        ),
    ]
