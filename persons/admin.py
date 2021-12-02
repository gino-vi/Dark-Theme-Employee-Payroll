from django.contrib import admin

# Register your models here.
from .models import Employee, Paystub

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id_number', 'first_name', 'last_name', 'email']
    search_fields = ['id_number', 'first_name', 'last_name', 'email']

class PaystubAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'employee_name', 'pay_period_start', 'pay_period_end']
    search_fields = ['pay_period_start', 'pay_period_end']

    def employee_name(self, obj):
        return str(obj.employee.first_name) + " " + str(obj.employee.last_name)
    

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Paystub, PaystubAdmin)