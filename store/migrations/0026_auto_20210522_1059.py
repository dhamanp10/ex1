# Generated by Django 3.2.3 on 2021-05-22 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20210522_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email_otp',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_otp',
        ),
    ]
