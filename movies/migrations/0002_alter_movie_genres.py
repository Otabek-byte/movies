# Generated by Django 4.1.6 on 2023-02-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.genre', verbose_name='Жанры'),
        ),
    ]
