# Generated by Django 2.2.6 on 2019-10-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliocatalogo', '0003_auto_20191026_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
