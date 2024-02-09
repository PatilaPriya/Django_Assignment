from django.shortcuts import render
from .models import employee
# Create your views here.
def Emp_details(request):
    # return HttpResponse("<h1>This is Employee Management Application</h1>")
    employee_details = employee.objects.all()
    return render(request, "Employee_management_App/home.html", {'emps': employee_details})