# Generated by Django 4.2.11 on 2024-04-12 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0020_alter_livros_options_livros_arranjador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 12, 8, 5, 34, 161156)),
        ),
    ]