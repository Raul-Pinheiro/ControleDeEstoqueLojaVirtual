# Generated by Django 3.1.1 on 2020-09-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEstoque', '0034_auto_20200911_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='foto_produto',
            field=models.ImageField(blank=True, null=True, upload_to='img/%d/%m/%Y/'),
        ),
    ]
