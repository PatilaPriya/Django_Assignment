from django.db import models
from Employee.models import employee
# Create your models here.
class task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=100)
    member = models.ManyToManyField(employee, related_name="employees")
    due_date = models.DateField()
    priority = models.IntegerField()

    def __str__(self):
        return str(self.task_id)

