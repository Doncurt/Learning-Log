# Generated by Django 2.0.4 on 2018-04-22 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entries'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entries',
            new_name='Entry',
        ),
    ]
