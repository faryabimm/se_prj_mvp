# Generated by Django 2.0.6 on 2018-06-10 14:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20180610_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 10, 14, 24, 17, 575665, tzinfo=utc)),
        ),
    ]
