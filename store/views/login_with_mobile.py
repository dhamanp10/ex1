from django.shortcuts import render, redirect,HttpResponseRedirect

from django.contrib.auth.hashers import  check_password

from store.models.customer import Customer
from django.views import View
from store.special_fun import OTP

def verify_otp(request):
    error_message = None
    entered_otp = request.POST.get('OTP')
    random_otp=Login_with_mobile.random_otp
    phone=Login_with_mobile.phone
    customer = Customer.get_customer_by_phone(phone)
    if entered_otp != None:
        if random_otp == entered_otp:
            request.session['customer'] = customer.id
            request.session['customer_name'] = customer.first_name + customer.last_name
            if Login_with_mobile.return_url:
                return HttpResponseRedirect(Login_with_mobile.return_url)
            else:
                Login_with_mobile.return_url = None
                del request.session['mobile_login_return_url']
                return redirect('homepage')
        else:
            error_message = 'Invalid OTP!!'
    else:
        error_message = 'Invalid OTP!!'

    return render(request, 'login_with_mobile.html', {'error': error_message})


class Login_with_mobile(View):
    return_url=None
    phone=None
    random_otp=None
    def get(self, request):
        Login_with_mobile.return_url=request.session.get('mobile_login_return_url')
        return render(request, 'login_with_mobile.html')

    def post(self, request):
        flag = 0
        error_message = None
        phone = request.POST.get('phone')
        Login_with_mobile.phone=phone



        customer = Customer.get_customer_by_phone(phone)
        Login_with_mobile.random_otp=str(OTP.generate_otp())
        body="EX1_Store OTP:"+str(Login_with_mobile.random_otp)

        if customer:
            flag = 1
            OTP.send_otp(body,phone)
        else:
            error_message = 'Mobile Number Invalid..!!'
        return render(request, 'login_with_mobile.html', {'error': error_message,'phone':phone,'flag':flag})



