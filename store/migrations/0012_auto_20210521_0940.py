# Generated by Django 3.2.3 on 2021-05-21 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order_payment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_id',
            new_name='razorpay_order_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_signature',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
