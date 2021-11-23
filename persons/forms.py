from django import forms

class EmployeeForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField()
    address = forms.CharField()
    birth_date = forms.DateField()
    email = forms.EmailField()
    id_number = forms.IntegerField()
    date_hired = forms.DateField()
    pay_rate = forms.DecimalField()
    active = forms.BooleanField()