from django.shortcuts import render, redirect

from django.contrib.auth.hashers import make_password

from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = request.session['phone']
        email = postData.get('email')
        password = postData.get('password')
        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            request.session['phone']=None
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if not customer.first_name:
            error_message = "First Name Requird !!"
        elif len(customer.first_name) < 3:
            error_message = "First Name must be 3 character long or more !!"
        elif not customer.last_name:
            error_message = "Last Name Requird !!"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 character long or more !!"
        elif not customer.phone:
            error_message = "Phone Number Required !!"
        elif len(customer.phone) != 10:
            error_message = "Phone Number Must Be 10 Digit long"
        elif not customer.email:
            error_message = "Email Required !!"
        elif len(customer.email) < 5:
            error_message = "Email must Be 5 character long"
        elif not customer.password:
            error_message = "Password Required !!"
        elif len(customer.password) < 6:
            error_message = "Password must Be 6 character long"
        elif customer.isExist():
            error_message = "Email Address Already Registered.."
        return error_message
