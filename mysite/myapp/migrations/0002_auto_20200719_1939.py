# Generated by Django 3.0.8 on 2020-07-19 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='device_info',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='device_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='device_price',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='im',
        ),
    ]
