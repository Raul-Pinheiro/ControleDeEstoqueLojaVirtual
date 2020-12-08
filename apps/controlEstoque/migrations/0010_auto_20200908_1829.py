# Generated by Django 3.1.1 on 2020-09-08 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEstoque', '0009_auto_20200908_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='data_ultima_compra',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 18, 29, 45, 399880)),
        ),
        migrations.AlterField(
            model_name='produtos_loja',
            name='foto_produto',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
