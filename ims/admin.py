from django.contrib import admin
from .models import Category,Profile,Product,Order,Stock,Notification

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Stock)
admin.site.register(Notification)