# Generated by Django 3.1.3 on 2020-11-04 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='airport_arrive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrive', to='flight.airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airport_depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dapart', to='flight.airport'),
        ),
    ]
