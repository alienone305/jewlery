# Generated by Django 3.2 on 2021-10-23 09:48

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_ordermodel_jdatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='jdatetime',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 10, 23, 13, 18, 25, 953561)),
        ),
    ]
