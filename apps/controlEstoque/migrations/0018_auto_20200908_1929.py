# Generated by Django 3.1.1 on 2020-09-08 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEstoque', '0017_auto_20200908_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='data_ultima_compra',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 19, 29, 28, 686019)),
        ),
    ]
