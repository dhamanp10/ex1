from django.shortcuts import render, redirect
from store.special_fun import OTP
from django.contrib.auth.hashers import  check_password
from store.models.orders import Order
from store.models.product import Product
from store.models.customer import Customer
from store.models.payments import Payment
from django.views import View
import razorpay
from django.views.decorators.csrf import csrf_exempt
from Eshop.settings import key_id,key_secret


def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


def price_total(product, cart):
    return product.price * cart_quantity(product, cart)


def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum = sum + price_total(p, cart)
    sum = sum * 100
    return sum

def cash_on_delivery(request):
    request.session['cart'] = {}
    return render(request, "success_order.html")

def success_order(request):
    return render(request, "success_order.html")


@csrf_exempt
def success(request):
    a = request.POST
    print(a)
    order_id = request.session.get('order_id')
    data={}

    customer = request.session.get('customer')
    cart = request.session.get('cart')
    products = Product.get_products_by_id(list(cart.keys()))
    amount = total_cart_price(products, cart)/100


    for key,val in a.items():
        if key == 'razorpay_order_id':
            data['razorpay_order_id'] = val
        elif key == 'razorpay_payment_id':
            data['razorpay_payment_id'] = val
        elif key == 'razorpay_signature':
            data['razorpay_signature'] = val
    client = razorpay.Client(auth=(key_id,key_secret))
    check = client.utility.verify_payment_signature(data)
    if check:
        return render(request,"error.html")
    else:
        address = Placeorder.pass_address
        phone = Placeorder.pass_phone
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        amount = total_cart_price(products, cart)
        for product in products:
            order = Order(customer =Customer(id=customer),
                          product = product,
                          price =product.price,
                          quantity =cart.get(str(product.id)),
                          address =address,
                          phone=phone,
                          razorpay_order_id=order_id,
                          paid=True)
            order.save()

        pay = Payment(
            amount=amount,
            customer =Customer(id=customer),
            razorpay_payment_id=data.get('razorpay_payment_id'),
            razorpay_order_id=data.get('razorpay_order_id'),
            razorpay_signature=data.get('razorpay_signature')

        )
        pay.save()
        request.session['cart'] = {}

        msg="EX1-Store Order Placed:Order ID: "+str(order_id)+" amounting to Rs."+str(amount)\
            +" with Payment ID: "+data.get('razorpay_payment_id')+" has been received and will be delivered shortly."
        OTP.send_otp(msg, phone)

    return render(request, "success_order.html",msg)



class Placeorder(View):
    pass_address=None
    pass_phone = None
    def post(self, request):
        error_message=None
        Placeorder.pass_address = request.POST.get('address')

        Placeorder.pass_phone = request.POST.get('phone')
        if not Placeorder.pass_phone:
            error_message = "Phone Number Required !!"
        elif len(Placeorder.pass_phone) != 10:
            error_message = "Phone Number Must Be 10 Digit long"
        elif not Placeorder.pass_phone.isdecimal():
            error_message = "Phone Number Must only number"
        elif not Placeorder.pass_address:
            error_message = "Address Requird !!"
        elif len(Placeorder.pass_address) < 10:
            error_message = "Address must be 10 character long or more !!"

        if not error_message:
            cart = request.session.get('cart')
            products = Product.get_products_by_id(list(cart.keys()))

            amount = total_cart_price(products, cart)

            client = razorpay.Client(auth=(key_id, key_secret))
            DATA = {
                'amount': amount,
                'currency': "INR",
                'receipt': "EX-1 Store payment",
                'notes': {
                    'name': "prateek",
                    'payment for': "clothes"
                },
                'payment_capture': "1"

            }
            payment = client.order.create(data=DATA)
            print(payment)
            request.session['order_id'] = payment['id']

            return render(request, "placeorder.html", payment)
        else:
            return render(request, "cart.html", {'error': error_message})







