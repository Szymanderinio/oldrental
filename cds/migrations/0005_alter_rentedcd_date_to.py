# Generated by Django 3.2.2 on 2021-06-03 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0004_alter_rentedcd_date_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentedcd',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 3, 20, 15, 34, 348217)),
        ),
    ]
