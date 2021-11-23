from typing_extensions import Required
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, EmailField

# Create your models here.
class Person(models.Model):
    id_number = models.IntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    middle_name = models.TextField(blank=True)
    address = models.TextField()
    birth_date = models.DateField()
    email = models.EmailField(('email address'), unique=True)

class Employee(Person):
    date_hired = models.DateField()
    pay_rate = models.FloatField()
    active = models.BooleanField()

class Paystub(models.Model):
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    hours_worked = models.FloatField() #Need to figure out how to connect this to the function below
    rate = models.FloatField() #Need to figure out how to connect this to the employee's rate
    gross_pay = models.IntegerField() 
    deductions = models.FloatField()
    taxes = models.FloatField() #Need to figure out how to connect this to the function below
    net_pay = models.FloatField() #Need to figure out how to connect this to the function below

    #Functions still need to be worked on
    def calculate_gross ():
        
        gross = 0.0
        return gross
    
    def calculate_taxes():
        taxes = 0.0
        return taxes

    def calculate_net():
        net = 0.0
        return net

class Schedule(models.Model):
    mon_start = models.FloatField(default=0)
    tue_start = models.FloatField(default=0)
    wed_start = models.FloatField(default=0)
    thu_start = models.FloatField(default=0)
    fri_start = models.FloatField(default=0)
    sat_start = models.FloatField(default=0)
    sun_start = models.FloatField(default=0)
