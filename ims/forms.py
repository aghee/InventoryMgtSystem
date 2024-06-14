from django.forms import ModelForm
from .models import Product,Order,ContactUs

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        exclude=["prodcateg"]

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=["user","product","status","quantity","supplier"]
        # exclude=["products","approved_by"]

class ContactUsForm(ModelForm):
    class Meta:
        model=ContactUs
        fields="__all__"