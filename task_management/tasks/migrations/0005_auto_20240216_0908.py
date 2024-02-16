# Generated by Django 3.1.4 on 2024-02-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_remove_employee_task_id'),
        ('tasks', '0004_auto_20240216_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='member',
            field=models.ManyToManyField(related_name='employees', to='Employee.employee'),
        ),
        migrations.DeleteModel(
            name='works_on',
        ),
    ]
