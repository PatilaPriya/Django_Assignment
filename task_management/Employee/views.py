from django.shortcuts import render, redirect
from .models import employee
from .models import employee
from django.contrib.auth.models import User


# Create your views here.
def Emp_details(request):
    # return HttpResponse("<h1>This is Employee Management Application</h1>")
    employee_details = employee.objects.all()
    return render(request, "Employee_management_App/home.html", {'emps': employee_details})

def add_employee(request):
    employee_details = {}
    if request.method == "POST":
        emp_id = request.POST.get('empid')
        emp_name = request.POST.get('empname')
        emp_email = request.POST.get('empemail')
        emp_dept = request.POST.get('empdept')
        emp_address = request.POST.get('empaddress')

        emp = employee(emp_id= emp_id, name=emp_name, email=emp_email, dept=emp_dept, address=emp_address)
        emp.save()

        user = User.objects.create(username=emp_name)
        user.set_password(emp_id)
        user.save()

        return redirect('/emp/')
    return render(request, "Employee_management_App/Employee_register.html")