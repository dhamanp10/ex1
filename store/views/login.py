from django.shortcuts import render, redirect,HttpResponseRedirect

from django.contrib.auth.hashers import  check_password

from store.models.customer import Customer
from django.views import View


class Login(View):
    return_url=None
    def get(self, request):
        Login.return_url=request.GET.get('return_url')
        request.session['mobile_login_return_url']=Login.return_url
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            if check_password(password, customer.password):
                request.session['customer']=customer.id
                request.session['customer_name'] = customer.first_name + customer.last_name


                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('homepage')
            else:
                error_message = 'Email Or Password Invalid..!!'
        else:
            error_message = 'Email Or Password Invalid..!!'
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
