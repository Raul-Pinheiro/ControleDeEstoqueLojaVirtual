# Generated by Django 3.1.1 on 2020-09-08 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEstoque', '0013_produtos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='vendedor',
        ),
        migrations.AlterField(
            model_name='produtos',
            name='data_ultima_compra',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 19, 14, 33, 383086)),
        ),
    ]
