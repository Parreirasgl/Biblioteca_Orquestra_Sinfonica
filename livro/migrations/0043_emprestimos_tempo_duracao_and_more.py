# Generated by Django 4.2.11 on 2024-05-10 13:21

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0042_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='duracao_emprestimo',
            field=models.DurationField(default=None),
            preserve_default=False,
        ),
    ]