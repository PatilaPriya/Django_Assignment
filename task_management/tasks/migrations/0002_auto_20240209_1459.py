# Generated by Django 3.1.4 on 2024-02-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='task_name',
        ),
    ]
