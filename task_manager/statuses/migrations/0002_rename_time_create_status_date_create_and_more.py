# Generated by Django 4.1.7 on 2023-03-27 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='time_create',
            new_name='date_create',
        ),
        migrations.RemoveField(
            model_name='status',
            name='time_update',
        ),
    ]