# Generated by Django 3.1.3 on 2021-06-16 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20210616_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='quest',
            new_name='post',
        ),
    ]