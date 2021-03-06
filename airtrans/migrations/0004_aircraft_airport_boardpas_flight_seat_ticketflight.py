# Generated by Django 3.0.5 on 2020-04-17 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airtrans', '0003_auto_20200417_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('aircraft_code', models.SlugField(max_length=10, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=10)),
                ('range', models.IntegerField()),
                ('seat_q', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_code', models.SlugField(max_length=10, primary_key=True, serialize=False)),
                ('airport_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.IntegerField(primary_key=True, serialize=False)),
                ('flight_no', models.IntegerField()),
                ('schedul_depar', models.DateTimeField()),
                ('schedul_arriv', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
                ('actual_depar', models.CharField(blank=True, max_length=10)),
                ('actual_arriv', models.CharField(blank=True, max_length=10)),
                ('aircraft_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Aircraft')),
                ('arriv_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport', to='airtrans.Airport')),
                ('depar_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_airport', to='airtrans.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='TicketFlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_condition', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Flight')),
                ('ticket_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Ticket')),
            ],
            options={
                'unique_together': {('ticket_no', 'flight_id')},
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.SlugField(max_length=10, unique=True)),
                ('fare_condition', models.CharField(max_length=10)),
                ('aircraft_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airtrans.Aircraft')),
            ],
            options={
                'unique_together': {('aircraft_code', 'seat_no')},
            },
        ),
        migrations.CreateModel(
            name='BoardPas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boarding_no', models.IntegerField()),
                ('seat_no', models.SlugField(max_length=10, unique=True)),
                ('flight_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bp_flight', to='airtrans.TicketFlight')),
                ('ticket_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bp_ticket', to='airtrans.TicketFlight')),
            ],
            options={
                'unique_together': {('ticket_no', 'flight_id')},
            },
        ),
    ]
