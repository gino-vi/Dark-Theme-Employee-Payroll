from typing import ContextManager
from django.shortcuts import render
from django import template
from django.http import HttpResponse
from .models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.
# **************************************************************************
@login_required
def add_employee_view(request):
    context = {}
    
    if request.method == "POST":
        emp_fname = request.POST.get("fname")
        emp_mname = request.POST.get("mname")
        emp_lname = request.POST.get("lname")
        emp_address = request.POST.get("address")
        emp_dob = request.POST.get("dob")
        emp_email = request.POST.get('email')
        emp_id = request.POST.get("id") #needs to be updated to auto generate
        emp_date_hired = request.POST.get("hired")
        emp_wage = request.POST.get("wage")


        Employee.objects.create(first_name = emp_fname, middle_name = emp_mname, last_name = emp_lname, address = emp_address,
                                birth_date = emp_dob, email = emp_email, id_number = emp_id, date_hired = emp_date_hired, pay_rate = emp_wage,
                                active = True)

        context['created'] = True

    HTML_STRING = render(request, "add-employee.html", context=context)

    return HttpResponse(HTML_STRING)

# **************************************************************************   
@login_required
def edit_employee_view(request):

    return HttpResponse("edit-employee.html")

# **************************************************************************
@login_required
def search_employee_view(request):
    query_dict = request.GET 

    try:
        id_number = int(query_dict.get("id"))
    except:
        id_number = None

    employee_obj = None

    if id_number is not None:
        employee_obj = Employee.objects.get(id=id_number)
    
    context = {
        "object": employee_obj
    }
    return render(request, "search-employee.html", context=context)

    # **************************************************************************

