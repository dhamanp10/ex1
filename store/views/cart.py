from django.shortcuts import render, redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from store.models.product import Product
from django.views import View


class Cart(View):
    def get(self, request):
        customer_id = request.session.get('customer')
        customer = Customer.get_customer_by_id(customer_id)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)

        return render(request, 'cart.html',{'products':products,'customer':customer})

    def post(self,request):
        customer_id = request.session.get('customer')
        customer = Customer.get_customer_by_id(customer_id)
        product=request.POST.get('product')
        remove= request.POST.get('remove')
        cart= request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1

                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1
        request.session['cart']=cart
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(request.session['cart'])
        return render(request, 'cart.html',{'products':products,'customer':customer})

