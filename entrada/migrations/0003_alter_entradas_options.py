# Generated by Django 4.0.2 on 2023-05-16 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0002_alter_entradas_produto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entradas',
            options={'ordering': ['-produto'], 'verbose_name': 'Entrada', 'verbose_name_plural': 'Entradas'},
        ),
    ]
