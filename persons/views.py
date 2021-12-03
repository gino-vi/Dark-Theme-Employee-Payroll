from typing import ContextManager
from django.shortcuts import render
from django import template
from django.http import HttpResponse
from .models import Employee, Paystub
from django.contrib.auth.decorators import login_required

# Create your views here.
# **************************************************************************
@login_required
def add_employee_view(request):
    context = {}
    lastEmployee = Employee.objects.latest("id_number")
    #print(lastEmployee)
    #print(lastEmployee.id_number)
    #print(lastEmployee.id_number + 1)

    if request.method == "POST":
        emp_fname = request.POST.get("fname")
        emp_mname = request.POST.get("mname")
        emp_lname = request.POST.get("lname")
        emp_address = request.POST.get("address")
        emp_dob = request.POST.get("dob")
        emp_email = request.POST.get('email')
        #emp_id = request.POST.get("id") #needs to be updated to auto generate
        emp_id = lastEmployee.id_number + 1
        emp_date_hired = request.POST.get("hired")
        emp_wage = request.POST.get("wage")

        Employee.objects.create(first_name = emp_fname, middle_name = emp_mname, last_name = emp_lname, address = emp_address,
                                birth_date = emp_dob, email = emp_email, id_number = emp_id, date_hired = emp_date_hired, pay_rate = emp_wage,
                                active = True)

        context['created'] = True


    return  render(request,'add-employee.html', context=context)


# **************************************************************************
@login_required
def edit_employee_view(request):
    context={}
    employees = Employee.objects.all()
    context = {
        'employees':employees,

    }



    return render(request,'edit-employee.html', context=context)

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
        employee_obj = Person.objects.get(id_number=id_number)

    context = {
        "object": employee_obj
    }
    return render(request, "search-employee.html", context=context)


    # **************************************************************************

@login_required
def view_employee_view(request):
    context={}
    employees = Employee.objects.all()
    context = {
        'employees':employees,

    }



    return render(request,'view-employee.html', context=context)

    # **************************************************************************

@login_required
def generate_paystub(request):
    employees = Employee.objects.all()
    context = {'employees':employees}

    if request.method == "POST":
        context = {}
        emp_id = request.POST.get("employeeBox")
        emp = Employee.objects.get(pk=emp_id)
        pstart = request.POST.get("so_period")
        pend = request.POST.get("eo_period")
        hworked = float(request.POST.get("total"))
        emp_rate = float(emp.pay_rate)
        emp_gross = calculate_gross(hworked, emp_rate)
        emp_tax = calculate_taxes(emp_rate, emp_gross)
        emp_net = calculate_net(emp_gross, emp_tax)
        Paystub.objects.create(employee = emp, pay_period_start = pstart, pay_period_end = pend,
                                hours_worked = hworked, rate = emp_rate, gross_pay = emp_gross,
                                taxes = emp_tax, net_pay = emp_net)
        context['created'] = True
    HTML_STRING = render(request, "generate-pay.html", context=context)
    return HttpResponse(HTML_STRING)

def calculate_gross(h, r):
    gross = h * r
    return gross

def calculate_taxes(r, g):
    weekly_salary = r*40
    annual_salary = weekly_salary*52

    if annual_salary < 9950:
        tax_rate = 0.1
    elif annual_salary < 40525:
        tax_rate = 0.12
    elif annual_salary < 86375:
        tax_rate = 0.22
    elif annual_salary < 164925:
        tax_rate = 0.24
    elif annual_salary < 209425:
        tax_rate = 0.32
    elif annual_salary < 523600:
        tax_rate = 0.35
    else:
        tax_rate = 0.37
    taxes = g*tax_rate
    return taxes

def calculate_net(g, t):
    net = g - t
    return net
