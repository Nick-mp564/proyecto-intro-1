# Generated by Django 4.2.5 on 2023-09-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_rename_cantidad_scorebar_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('compartidos', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Usuario',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Scorebar',
        ),
    ]
