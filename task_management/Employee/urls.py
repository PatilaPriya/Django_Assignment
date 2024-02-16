from django.urls import path
from .views import Emp_details, add_employee

urlpatterns = [
    path('', Emp_details, name="emp_details"),
    path('add_emp/', add_employee, name="add_emp")
]
