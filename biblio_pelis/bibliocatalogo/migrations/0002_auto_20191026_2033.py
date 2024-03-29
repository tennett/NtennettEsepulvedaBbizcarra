# Generated by Django 2.2.6 on 2019-10-26 23:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bibliocatalogo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='nom',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='año',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='genero',
            field=models.CharField(help_text='Genero de la', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='nombre_pelicula',
            field=models.CharField(help_text='Nombre de pelicula', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Codigo de pelicula', primary_key=True, serialize=False),
        ),
    ]
