# Generated by Django 3.2.1 on 2021-05-06 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titles',
            new_name='title',
        ),
    ]
