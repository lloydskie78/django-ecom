# Generated by Django 3.1.5 on 2021-01-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_payment_intent'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='used_coupon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
