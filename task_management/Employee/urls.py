from django.urls import path
from .views import Emp_details

urlpatterns = [
    path('', Emp_details),
]
