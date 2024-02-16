from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dept = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return str(self.emp_id)
