from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Profile(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,null=True,blank=True)
    phone_number = PhoneNumberField(unique=True,max_length=10)

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True,blank=True)

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True,blank=True)
    price=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(999999)])
    supplier=models.CharField(max_length=50)
    quantity=models.IntegerField(validators=[MinValueValidator(0)]) #non-negative quantities not allowed
    categories=models.ManyToManyField(Category,through="ProductCategory")

class ProductCategory(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

class Stock(models.Model):
    product_id=models.OneToOneField(Product,on_delete=models.CASCADE,primary_key=True)
    quantity=models.IntegerField(validators=[MinValueValidator(0)])
    reorder_level=models.IntegerField(validators=[MinValueValidator(0)])

class Order(models.Model):
    STATUS=(
        ("order-placed","order-placed"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
    )
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_by")
    status=models.CharField(max_length=50,choices=STATUS)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    approved_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="approved_orders")
    products=models.ManyToManyField(Product,through="OrderProduct")

class OrderProduct(models.Model):
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(validators=[MinValueValidator(0)])

class Notification(models.Model):
    stock_id=models.ForeignKey(Stock,on_delete=models.CASCADE)
    message=models.CharField(max_length=250)
