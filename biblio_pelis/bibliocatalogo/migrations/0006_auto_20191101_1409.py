# Generated by Django 2.2.6 on 2019-11-01 17:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bibliocatalogo', '0005_auto_20191101_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
