# Generated by Django 3.1.1 on 2020-09-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlEstoque', '0028_remove_produtos_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='foto_produto',
            field=models.ImageField(blank=True, upload_to='fotografias/%d/%m/%Y'),
        ),
    ]
