# Generated by Django 4.2.5 on 2023-10-24 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_remove_publicacion_compartidos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='email',
        ),
    ]
