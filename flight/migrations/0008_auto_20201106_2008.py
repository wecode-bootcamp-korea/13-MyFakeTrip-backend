# Generated by Django 3.1.3 on 2020-11-06 11:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0007_flight_remain_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='basic_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='flight',
            name='seat_class',
            field=models.CharField(default=django.utils.timezone.now, max_length=45),
            preserve_default=False,
        ),
    ]