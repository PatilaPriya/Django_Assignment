# Generated by Django 3.1.4 on 2024-02-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dept', models.CharField(max_length=20)),
                ('task_id', models.CharField(max_length=20)),
                ('working', models.BooleanField(default=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
