from django.db import models
from .customer import Customer
import datetime


class Payment(models.Model):
    amount = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    razorpay_payment_id = models.CharField(max_length=100, default='', blank=True)
    razorpay_order_id = models.CharField(max_length=100, default='', blank=True)
    razorpay_signature = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField(default=datetime.datetime.now)


    @staticmethod
    def payment_success(self):
        self.save()

    @staticmethod
    def get_payment_by_id(payment_id):
        try:
            return Payment.objects.get(id=payment_id)
        except:
            return False
