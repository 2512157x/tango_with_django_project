# Generated by Django 2.1.5 on 2021-07-29 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210730_0025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={},
        ),
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
