# Generated by Django 4.2.5 on 2023-09-27 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_scorebar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scorebar',
            old_name='cantidad',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='psw',
        ),
    ]
