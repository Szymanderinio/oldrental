# Generated by Django 3.2.2 on 2021-05-31 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0002_alter_rentedcd_date_to'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre',
            new_name='CDGenre',
        ),
        migrations.AlterField(
            model_name='rentedcd',
            name='date_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 21, 32, 59, 138424)),
        ),
    ]
