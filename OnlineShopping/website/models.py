from django.db import models
import datetime


# Model Category
class Category(models.Model):
    name = models.CharField(max_length=50)
    @staticmethod
    def all_categories():
        return Category.objects.all()
    def __str__(self) -> str:
        return self.name

# Model Products
class Products(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=100,blank=True,null=True)
    image=models.ImageField(upload_to='media/products/')
    @staticmethod
    def product_by_id(key):
            return Products.objects.filter(id__in=key)
    @staticmethod
    def all_products():
        return Products.objects.all()
    @staticmethod
    def products_by_category(key):
        if key:
            return Products.objects.filter(category=key)
        else:
            return Products.all_products()

# Model Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    def register(self):
        self.save()
    @staticmethod
    def current_customer(key):
        return Customer.objects.get(id=key)
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False


# Model Order
class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    def placeOrder(self):
        self.save()
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')