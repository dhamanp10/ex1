from django.db import models
from .product import Product
from .customer import Customer
from .payments import Payment
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=100, default='', blank=True)
    razorpay_order_id = models.CharField(max_length=100, default='', blank=True)
    paid = models.BooleanField(default=False)



    @staticmethod
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order \
            .objects \
            .filter(customer=customer_id) \
            .order_by('-date')


    @staticmethod
    def get_orders_by_razorpay_order_id(order_id):
        return Order.objects.filter(razorpay_order_id=order_id)
