# Generated by Django 2.2.6 on 2019-11-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliocatalogo', '0006_auto_20191101_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
