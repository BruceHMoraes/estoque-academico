# Generated by Django 4.0.2 on 2023-05-15 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Preço')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produto.cores', verbose_name='Produto')),
            ],
        ),
    ]
