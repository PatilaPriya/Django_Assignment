# Generated by Django 3.1.4 on 2024-02-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('task_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('member', models.CharField(max_length=20)),
                ('due_date', models.DateField()),
                ('priority', models.IntegerField()),
            ],
        ),
    ]
