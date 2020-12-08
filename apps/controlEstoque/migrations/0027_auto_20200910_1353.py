# Generated by Django 3.1.1 on 2020-09-10 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlEstoque', '0026_produtos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produtos',
            old_name='unity',
            new_name='medida',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='data_ultima_compra',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='estoque_atual',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='estoque_maximo',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='estoque_minimo',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='ultimo_preço_compra',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='valor_venda',
        ),
    ]
