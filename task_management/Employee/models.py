from django.db import models
from tasks.models import task

# Create your models here.
class employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dept = models.CharField(max_length=20)
    #task_id = models.IntegerField()
    task_id = models.ForeignKey(task, on_delete=models.CASCADE)
    address = models.TextField()

