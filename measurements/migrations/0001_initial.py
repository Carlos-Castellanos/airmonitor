# Generated by Django 4.1.2 on 2022-10-30 03:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sensors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Measurements",
            fields=[
                (
                    "idSensor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="sensors.sensor",
                    ),
                ),
                (
                    "measurementDate",
                    models.DateField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "measurementTime",
                    models.TimeField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "Latitude",
                    models.DecimalField(decimal_places=7, default=0, max_digits=10),
                ),
                (
                    "Longitude",
                    models.DecimalField(decimal_places=7, default=0, max_digits=10),
                ),
                (
                    "Temperature",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "Humidity",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "Pression",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "PM25",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "PM10",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name": "Measurement",
                "verbose_name_plural": "measurements",
                "ordering": ["measurementDate", "measurementTime", "idSensor"],
            },
        ),
    ]
