# Generated by Django 2.1.3 on 2019-05-21 19:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snoop', '0007_auto_20190522_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportpost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 19, 13, 0, 249776, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='sawpost',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 21, 19, 13, 0, 558949, tzinfo=utc), editable=False),
        ),
    ]
