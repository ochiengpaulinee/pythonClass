# Generated by Django 4.2.3 on 2023-07-10 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
        ('order', '0002_order_cart_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.delivery'),
        ),
    ]
