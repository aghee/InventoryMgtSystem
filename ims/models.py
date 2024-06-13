from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True) #user_id
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,null=True,blank=True,verbose_name="Email address")
    phone_number = PhoneNumberField(unique=True,max_length=15)

    def __str__(self):
        return self.first_name + " " + self.last_name 

class Category(models.Model):
    name=models.CharField(max_length=50,verbose_name="Product_Category")
    description=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50,verbose_name="Item Name")
    prodcateg=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="prod_cat",verbose_name="Category",default=6)
    description=models.TextField(null=True,blank=True)
    price=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(999999)],verbose_name="Price per piece")
    supplier=models.CharField(max_length=50,verbose_name="Supplier Name")
    quantity=models.IntegerField(validators=[MinValueValidator(0)],verbose_name="Quantity-In-Stock") #non-negative quantities not allowed
    categories=models.ManyToManyField(Category,through="ProductCategory")

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE) #product_id
    category=models.ForeignKey(Category,on_delete=models.CASCADE) #category_id

class Stock(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE,primary_key=True) #product_id
    quantity=models.IntegerField(validators=[MinValueValidator(0)])
    reorder_level=models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name="Stock"
        verbose_name_plural="Stock"
    
    def __str__(self):
        return self.product.name

class Order(models.Model):
    STATUS=(
        ("order-placed","order-placed"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="created_by",verbose_name="Ordered By",default=1) #user_id
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product",verbose_name="Product-to-order",default=1) #product_id
    status=models.CharField(max_length=50,choices=STATUS,verbose_name="Order  Status")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    approved_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="approved_orders",verbose_name="Approved By")
    products=models.ManyToManyField(Product,through="OrderProduct")

    class Meta:
        ordering=["-updated","-updated"]

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderProduct(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE) #order_id
    product=models.ForeignKey(Product,on_delete=models.CASCADE) #product_id
    quantity=models.IntegerField(validators=[MinValueValidator(0)])

class Notification(models.Model):
    stock=models.ForeignKey(Stock,on_delete=models.CASCADE) #stock_id
    message=models.CharField(max_length=250)
    
    def __str__(self):
        return self.message[:30]
    
