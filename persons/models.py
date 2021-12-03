from typing_extensions import Required
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, EmailField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Person(models.Model):
    id_number = models.IntegerField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    middle_name = models.TextField(blank=True)
    address = models.TextField()
    birth_date = models.DateField()
    email = models.EmailField(('email address'), unique=True)

class Employee(Person):
    date_hired = models.DateField()
    pay_rate = models.DecimalField(max_digits=7, decimal_places=2)
    active = models.BooleanField()

class Paystub(models.Model):
    #Functions still need to be worked on
    employee = models.ForeignKey(Employee, default=None, on_delete=models.CASCADE)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2) #Need to figure out how to connect this to the function below
    rate = models.DecimalField(max_digits=7, decimal_places=2) #Need to figure out how to connect this to the employee's rate
    gross_pay = models.DecimalField(max_digits=7, decimal_places=2)
    #deductions = models.FloatField()
    taxes = models.DecimalField(max_digits=7, decimal_places=2) #Need to figure out how to connect this to the function below
    net_pay = models.DecimalField(max_digits=7, decimal_places=2)#Need to figure out how to connect this to the function below

class Schedule(models.Model):
    day1 = models.FloatField(default=0)
    day2 = models.FloatField(default=0)
    day3 = models.FloatField(default=0)
    day4 = models.FloatField(default=0)
    day5 = models.FloatField(default=0)
    day6 = models.FloatField(default=0)
    day7 = models.FloatField(default=0)
    day8 = models.FloatField(default=0)
    day9 = models.FloatField(default=0)
    day10 = models.FloatField(default=0)
    day11 = models.FloatField(default=0)
    day12 = models.FloatField(default=0)
    day13 = models.FloatField(default=0)
    day14 = models.FloatField(default=0)
    day15 = models.FloatField(default=0)
