# Generated by Django 3.1.3 on 2020-11-03 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('logo', models.URLField()),
            ],
            options={
                'db_table': 'airlines',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightid', models.CharField(max_length=45)),
                ('airport_depart', models.CharField(max_length=45)),
                ('airport_arrive', models.CharField(max_length=45)),
                ('depart_time', models.TimeField()),
                ('arrive_time', models.TimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.airline')),
            ],
            options={
                'db_table': 'flights',
            },
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'weekdays',
            },
        ),
        migrations.CreateModel(
            name='FlightWeekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
                ('weekday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.weekday')),
            ],
            options={
                'db_table': 'flight_weekdays',
            },
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_weekday',
            field=models.ManyToManyField(through='flight.FlightWeekday', to='flight.Weekday'),
        ),
    ]
