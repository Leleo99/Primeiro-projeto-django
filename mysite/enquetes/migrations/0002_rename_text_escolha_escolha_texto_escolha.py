# Generated by Django 5.0.6 on 2024-06-14 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='escolha',
            old_name='text_escolha',
            new_name='texto_escolha',
        ),
    ]
