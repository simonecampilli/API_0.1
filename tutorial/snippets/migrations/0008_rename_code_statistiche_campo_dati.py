# Generated by Django 4.0.4 on 2022-11-30 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_statistiche'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistiche',
            old_name='code',
            new_name='campo_dati',
        ),
    ]