# Generated by Django 3.2.2 on 2021-05-31 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentedcd',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 21, 19, 33, 143587)),
        ),
    ]
