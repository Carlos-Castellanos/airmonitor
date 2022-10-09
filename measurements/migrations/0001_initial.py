# Generated by Django 4.1.1 on 2022-10-09 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Measurements",
            fields=[
                ("name", models.CharField(max_length=10)),
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
                    models.DecimalField(decimal_places=5, default=0, max_digits=8),
                ),
                (
                    "Longitude",
                    models.DecimalField(decimal_places=5, default=0, max_digits=8),
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
                "ordering": ["id"],
            },
        ),
    ]
