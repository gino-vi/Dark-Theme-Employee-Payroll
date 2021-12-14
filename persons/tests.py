from django.contrib.auth import get_user_model
from django.http import response
from django.test import TestCase
from persons.models import Employee, Person, Paystub

# Create your tests here.
User = get_user_model()

#Test Employee Creation
class EmployeeTestCase(TestCase):

    def setUp(self):
        #Create User
        employee_a = Employee(first_name = "John", middle_name = "", last_name = "Doe", address = "123 Main St. Downtown, CA 90001",
                                birth_date = "2021-11-22", email = "jdoe@email.com", id_number = 10, date_hired = "2021-11-22", pay_rate = 15.00,
                                active = True)
        print(employee_a.id_number) #Check Data is corrent
        employee_a.save() #Temp save the model

        #Make sure count of employees not 0
    def test_employee_exists(self):
        employee_count = Employee.objects.all().count() 
        print(employee_count)
        self.assertEqual(employee_count, 1)
        self.assertNotEqual(employee_count, 0)

#Test Add Employee Page
class add_employee_test(TestCase):
    #Set up admid user
    def setUp(self):
        user_a = User(username ="testa", email="")
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password("123password")
        user_a.save()
        self.user_a = user_a
   
    #Try to create employee without proper credentials
    def test_invalid_request(self):
        self.client.login(username = "Noneuser", password = "123password")
        response = self.client.post("/create", {"fname":"John", "mname":"", "lname":"Doe", "address":"123 Main St",
                                                "dob":"2000-01-01", "email":"jdoe@email.com", "hired":"2021-01-01", 
                                                "wage": 15.00})
        self.assertNotEqual(response.status_code, 200)
        print(response.status_code)
    
    #Try to create employee with proper credentials
    def test_valid_request(self):
        self.client.login(username = self.user_a.username, password = "123password")
        response = self.client.post("/create", {"fname":"John", "mname":"", "lname":"Doe", "address":"123 Main St",
                                                "dob":"2000-01-01", "email":"jdoe@email.com", "hired":"2021-01-01", 
                                                "wage": 15.00})
        self.assertEqual(response.status_code, 200)
        print(response.status_code)

class search_employee_test(TestCase):
    
    def setUp(self):
        #Create Superuser
        user_a = User(username ="testa", email="")
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password("123password")
        user_a.save()
        self.user_a = user_a
        #Create User
        employee_a = Employee(first_name = "John", middle_name = "", last_name = "Doe", address = "123 Main St. Downtown, CA 90001",
                                birth_date = "2021-11-22", email = "jdoe@email.com", id_number = 10, date_hired = "2021-11-22", pay_rate = 15.00,
                                active = True)
        print(employee_a.id_number) #Check Data is corrent
        employee_a.save() #Temp save the model

    #Try to search employee without proper credentials
    def test_invalid_search(self):
        self.client.login(username = "Noneuser", password = "123password")
        response = self.client.get("/search", {"fname":"John", "lname":"Doe"})
        self.assertNotEqual(response.status_code, 200)
        print(response.status_code)
    
    #Try to search employee with proper credentials
    def test_valid_search(self):
        self.client.login(username = self.user_a.username, password = "123password")
        response = self.client.get("/search", {"fname":"John", "lname":"Doe"})
        self.assertEqual(response.status_code, 200)
        print(response.status_code)

#Test Paystub Creation
class PaystubTestCase(TestCase):

    def setUp(self):
        #Create User
        employee_b = Employee(first_name = "John", middle_name = "", last_name = "Doe", address = "123 Main St. Downtown, CA 90001",
                                birth_date = "2021-11-22", email = "jdoe@email.com", id_number = 10, date_hired = "2021-11-22", pay_rate = 15.00,
                                active = True)
        employee_b.save() #Save
        #Create Paystub
        paystub_1 = Paystub(employee = employee_b, pay_period_start = "2021-11-01", pay_period_end = "2021-11-15",
                                hours_worked = 88, rate = 15, gross_pay = 1320,
                                taxes = 158.4, net_pay = 1161.6)
        print(paystub_1.net_pay)
        paystub_1.save() #Save

        #Make sure count of paystubs not 0
    def test_paystub_exists(self):
        paystub_count = Paystub.objects.all().count()
        print(paystub_count)
        self.assertEqual(paystub_count, 1)
        self.assertNotEqual(paystub_count, 0)

class view_paystub_test(TestCase):
    def setUp(self):
        #Create Superuser
        user_a = User(username ="testa", email="")
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password("123password")
        user_a.save()
        self.user_a = user_a

        #Create User
        employee_b = Employee(first_name = "John", middle_name = "", last_name = "Doe", address = "123 Main St. Downtown, CA 90001",
                                birth_date = "2021-11-22", email = "jdoe@email.com", id_number = 10, date_hired = "2021-11-22", pay_rate = 15.00,
                                active = True)
        employee_b.save() #Save
        self.employee_b = employee_b
        #Create Paystub
        paystub_1 = Paystub(employee = employee_b, pay_period_start = "2021-11-01", pay_period_end = "2021-11-15",
                                hours_worked = 88, rate = 15, gross_pay = 1320,
                                taxes = 158.4, net_pay = 1161.6)
        print(paystub_1.net_pay)
        paystub_1.save() #Save
    
    #Try to search employee without proper credentials
    def test_invalid_search(self):
        self.client.login(username = "Noneuser", password = "123password")
        response = self.client.get("/paystubs/" + str(self.employee_b.id_number) + "/" )
        self.assertNotEqual(response.status_code, 200)
        print(response.status_code)
    
    #Try to search employee with proper credentials
    def test_valid_search(self):
        self.client.login(username = self.user_a.username, password = "123password")
        response = self.client.get("/paystubs/" + str(self.employee_b.id_number) + "/" )
        self.assertEqual(response.status_code, 200)
        print(response.status_code)