# Generated by Django 3.2.3 on 2021-05-20 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.payment'),
            preserve_default=False,
        ),
    ]
