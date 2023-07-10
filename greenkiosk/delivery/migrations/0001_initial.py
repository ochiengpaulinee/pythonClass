# Generated by Django 4.2.3 on 2023-07-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=32)),
                ('contact_number', models.IntegerField()),
                ('delivery_date', models.DateTimeField()),
                ('delivery_time', models.TimeField()),
                ('delivery_driver_name', models.CharField(max_length=32)),
                ('delivery_address', models.CharField(max_length=32)),
                ('delivery_status', models.CharField(max_length=32)),
            ],
        ),
    ]
