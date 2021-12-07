"""
To render HTML webpages
"""
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from persons.models import Employee, Paystub

def home_view(request):
    employees = Employee.objects.all()
    user_count = Employee.objects.count()
    paystub_count = Paystub.objects.count()
    context = {
        "employees": employees,
        'user_count' : user_count,
        'paystub_count' : paystub_count
    }
    #print(employees)
    return render(request, "home-view.html", context=context)
