# Generated by Django 2.1.3 on 2019-05-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snoop', '0011_auto_20190525_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportpost',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sawpost',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
