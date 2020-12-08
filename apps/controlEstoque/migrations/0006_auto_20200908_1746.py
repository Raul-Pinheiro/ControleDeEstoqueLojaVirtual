# Generated by Django 3.1.1 on 2020-09-08 20:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_remove_criaadm_cadastro_senha_admin'),
        ('controlEstoque', '0005_auto_20200907_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='data_ultima_compra',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 17, 46, 8, 855604)),
        ),
        migrations.CreateModel(
            name='Produtos_loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=200)),
                ('unidade', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=200)),
                ('descricao', models.TextField(max_length=200)),
                ('estoque_atual', models.IntegerField()),
                ('quantidade_por_embalagem', models.IntegerField()),
                ('valor_venda', models.IntegerField()),
                ('foto_produto', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('publicada', models.BooleanField(default=False)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.criaadm')),
            ],
        ),
    ]
