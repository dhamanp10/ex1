from django.shortcuts import render, redirect,HttpResponseRedirect

from django.contrib.auth.hashers import  check_password

from store.models.customer import Customer
from django.views import View
from store.special_fun import OTP

def signup_verify_otp(request):
    error_message = None
    entered_otp = request.POST.get('OTP')
    random_otp=Signup_mobile.random_otp


    if entered_otp != None:
        if random_otp == entered_otp:
            if Signup_mobile.return_url:
                return HttpResponseRedirect(Signup_mobile.return_url)
            else:
                Signup_mobile.return_url = None
                del request.session['mobile_login_return_url']
                return redirect('signup')
        else:
            error_message = 'Invalid OTP!!'
    else:
        error_message = 'Invalid OTP!!'

    return render(request, 'signup_mobile.html', {'error': error_message,'phone':Signup_mobile.phone})


class Signup_mobile(View):
    return_url=None
    phone=None
    random_otp=None
    def get(self, request):
        Signup_mobile.return_url = request.GET.get('return_url')

        return render(request, 'signup_mobile.html')

    def post(self, request):
        error_message = None
        flag=0
        Signup_mobile.phone = request.POST.get('phone')


        if not Signup_mobile.phone:
            error_message = "Phone Number Required !!"
        elif len(Signup_mobile.phone) != 10:
            error_message = "Phone Number Must Be 10 Digit long"
        elif not Signup_mobile.phone.isdecimal():
            error_message = "Phone Number Must only number"


        if not error_message:
            request.session['phone'] = Signup_mobile.phone
            customer = Customer.get_customer_by_phone(Signup_mobile.phone)
            Signup_mobile.random_otp= str(OTP.generate_otp())
            body = "EX1_Store OTP:" + str(Signup_mobile.random_otp)

            if customer:
                error_message = 'Account with this number Already exists..!!'
            else:
                OTP.send_otp(body, Signup_mobile.phone)
                flag=1

        return render(request, 'signup_mobile.html', {'error': error_message,'phone':Signup_mobile.phone,'flag':flag})



