# Generated by Django 3.1.1 on 2020-09-08 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEstoque', '0006_auto_20200908_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='foto_produto',
        ),
        migrations.AlterField(
            model_name='produtos',
            name='data_ultima_compra',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 18, 8, 38, 392444)),
        ),
    ]
