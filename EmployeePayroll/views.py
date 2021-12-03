"""
To render HTML webpages
"""
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from persons.models import Employee

def home_view(request):
    employees = Employee.objects.all()
    context = {
        "employees": employees
    }
    print(employees)
    return render(request, "home-view.html", context=context)