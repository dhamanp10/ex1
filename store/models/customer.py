from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=500,default='')


    def register(self):
        self.save()
    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_customer_by_id(customer_id):
        try:
            return Customer.objects.get(id=customer_id)
        except:
            return False

    @staticmethod
    def get_customer_by_phone(customer_phone):
        try:
            return Customer.objects.get(phone=customer_phone)
        except:
            return False






