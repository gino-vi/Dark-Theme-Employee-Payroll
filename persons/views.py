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
    newEmployee_obj = None
    lastEmployee = None

    try:
        lastEmployee = Employee.objects.latest("id_number")
        lastEmpID = lastEmployee.id_number
    except:
        lastEmpID = 0

    if request.method == "POST":
        emp_fname = request.POST.get("fname")
        emp_mname = request.POST.get("mname")
        emp_lname = request.POST.get("lname")
        emp_address = request.POST.get("address")
        emp_dob = request.POST.get("dob")
        emp_email = request.POST.get('email')
        emp_id = lastEmpID + 1
        emp_date_hired = request.POST.get("hired")
        emp_wage = request.POST.get("wage")

        newEmployee_obj = Employee.objects.create(first_name = emp_fname, middle_name = emp_mname, last_name = emp_lname, address = emp_address,
                                birth_date = emp_dob, email = emp_email, id_number = emp_id, date_hired = emp_date_hired, pay_rate = emp_wage,
                                active = True)

        #context['created'] = True
        if newEmployee_obj is not None:
            context = {
                "object": newEmployee_obj
            }
        else:
            context = {}

        return render(request,'view-employee.html', context=context)


    return  render(request,'add-employee.html', context=context)


# **************************************************************************
@login_required
def edit_employee_view(request,id=None):
    context = {}
    employee_obj = None
    if id is not None:
        employee_obj = Employee.objects.get(id_number=id)
        ##print(employee_obj.birth_date)
        ##print(employee_obj.address)
    context = {
        "object": employee_obj,
    }

    if request.method == "POST":
        emp_active = request.POST.get("active")
        emp_fname = request.POST.get("fname")
        emp_mname = request.POST.get("mname")
        emp_lname = request.POST.get("lname")
        emp_address = request.POST.get("address")
        emp_email = request.POST.get("email")
        emp_wage = request.POST.get("wage")
        print(emp_active)
        if emp_active == 'Active':
            employee_obj.active = True
        else:
            employee_obj.active = False
        employee_obj.first_name = emp_fname
        employee_obj.middle_name = emp_mname
        employee_obj.last_name = emp_lname
        employee_obj.address = emp_address
        employee_obj.email = emp_email
        employee_obj.pay_rate = emp_wage

        employee_obj.save()

        return render(request,'view-employee.html', context=context)

    return render(request,'edit-employee.html', context=context)

# **************************************************************************
@login_required
def search_employee_view(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees
    }

    if request.method == "GET":
        emp_fname = request.GET.get("fname")
        emp_lname = request.GET.get("lname")

    if isNotBlank(emp_fname):
        employees = Employee.objects.filter(first_name = emp_fname)
        context = {
            "employees": employees
        }
    elif isNotBlank(emp_lname):
        employees = Employee.objects.filter(last_name = emp_lname)
        context = {
            "employees": employees
        }
    elif isBlank(emp_fname) and isBlank(emp_lname):
        employees = Employee.objects.all()
        context = {
            "employees": employees
        }

    return render(request, "search-employee.html", context=context)

def isBlank(myString):
    return not (myString and myString.strip())

def isNotBlank(myString):
    return bool(myString and myString.strip())

    # **************************************************************************

@login_required
def view_employee_view(request, id=None):
    employee_obj = None
    if id is not None:
        employee_obj = Employee.objects.get(id_number=id)
    context= {
    'object': employee_obj,
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
        
        employee_paystubs = Paystub.objects.filter(employee=emp).order_by('-pay_period_start')
        context = {
            "employee": emp,
            "employee_paystubs": employee_paystubs
        }
        return render(request,'employee-paystubs-list.html', context=context)

    return render(request, "generate-pay.html", context=context)

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

# **************************************************************************
def view_paystubs_view(request,id=None):
    context={}
    employee_obj = None
    employee_paystubs = None
    if id is not None:
        employee_obj = Employee.objects.get(id_number=id)
        if employee_obj is not None:
            employee_paystubs = Paystub.objects.filter(employee=employee_obj).order_by('-pay_period_start')

            context = {
                    "employee": employee_obj,
                    "employee_paystubs": employee_paystubs
                }        
    

    return render(request,'employee-paystubs-list.html', context=context)

# **************************************************************************
