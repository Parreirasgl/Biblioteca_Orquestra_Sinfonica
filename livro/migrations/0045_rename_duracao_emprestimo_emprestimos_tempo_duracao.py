# Generated by Django 4.2.11 on 2024-05-10 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0044_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimos',
            old_name='duracao_emprestimo',
            new_name='tempo_duracao',
        ),
    ]