from django.db import models

# Create your models here.
class task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=100)
    member = models.CharField(max_length=20)
    due_date = models.DateField()
    priority = models.IntegerField()

    def __str__(self):
        return str(self.task_id)