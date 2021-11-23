from django.contrib import admin

# Register your models here.
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id_number', 'first_name', 'last_name', 'email']
    search_fields = ['id_number', 'first_name', 'last_name', 'email']

admin.site.register(Employee, EmployeeAdmin)