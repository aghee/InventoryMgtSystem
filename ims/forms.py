from django.forms import ModelForm
from .models import Product,Order

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