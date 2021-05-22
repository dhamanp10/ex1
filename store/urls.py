"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, signup, login,cart,placeorder,orders,my_details,product_details,login_with_mobile,signup_mobile
from .views.login import logout
from .middlewares.auth import auth_middleware
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('placeorder', placeorder.Placeorder.as_view(), name='placeorder'),
    path('orders', auth_middleware(orders.OrdersView.as_view()), name='orders'),
    path('my_details', my_details.My_details.as_view(), name='my_details'),
    path('cash_on_delivery', placeorder.cash_on_delivery),
    path('success', placeorder.success),
    path('success_order', placeorder.success_order),
    path('product_details', product_details.product_details.as_view(), name='product_details'),
    path('login_with_mobile', login_with_mobile.Login_with_mobile.as_view(), name='login_with_mobile'),
    path('verify_otp', login_with_mobile.verify_otp, name='verify_otp'),
    path('signup_mobile', signup_mobile.Signup_mobile.as_view(), name='signup_mobile'),
    path('signup_verify_otp', signup_mobile.signup_verify_otp, name='signup_verify_otp'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
