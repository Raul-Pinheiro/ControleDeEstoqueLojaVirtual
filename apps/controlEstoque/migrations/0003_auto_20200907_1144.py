# Generated by Django 3.1.1 on 2020-09-07 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEstoque', '0002_auto_20200907_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='data_ultima_compra',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 7, 11, 44, 40, 516867)),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='ultimo_preço_compra',
            field=models.IntegerField(),
        ),
    ]
