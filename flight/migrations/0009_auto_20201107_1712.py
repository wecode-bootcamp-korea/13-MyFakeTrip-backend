# Generated by Django 3.1.3 on 2020-11-07 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0008_auto_20201106_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='airport_depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='flight.airport'),
        ),
    ]