from typing_extensions import Required
from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    middle_name = models.TextField(blank=True)
    address = models.TextField()
    birth_date = models.DateField()
    email = models.EmailField(('email address'), unique=True)

class Employee(Person):
    id_number = models.IntegerField()
    date_hired = models.DateField()
    pay_rate = models.FloatField()
    active = models.BooleanField()