from django.shortcuts import render, redirect

from django.contrib.auth.hashers import make_password

from store.models.customer import Customer
from django.views import View


class product_details(View):
    def get(self, request):
        return render(request, 'product_details.html')

    def post(self, request):
        postData = request.POST

        address = postData.get('address')


        # validation
        error_message=False
        if not address:
            error_message = "Provide Address to Update !!"
        elif len(address) < 10:
            error_message = "Address must be 10 character long or more !!"



        customer_id = request.session.get('customer')
        customer = Customer.get_customer_by_id(customer_id)
        value = {
            'error': error_message,
            'customer':customer,

        }

        # saving
        if not error_message:
            customer.address = address
            customer.register()
            return redirect('my_details')
        else:
            return render(request, 'my_details.html', value)


