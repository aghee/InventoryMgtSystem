from django.shortcuts import render,redirect
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registerUser(request):
    form=UserCreationForm()
    if request.method =="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("/")
    context={
        "form":form
    }
    return render(request,"ims/register.html",context)

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # try:
        #     user=User.objects.get(username=username)
        
        # except ObjectDoesNotExist:
        #     messages.error(request,"Username does not exist!")
        
        if username and password:
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password")

    context={}
    return render(request,"ims/login.html",context)

def logoutUser(request):
    logout(request)
    return redirect("login")


def home(request):
    products=Product.objects.all()
    context={
    "products":products
    }
    return render(request,"ims/home.html",context)

class ProductDetail(DetailView):
    model=Product
    template_name="ims/prod_detail.html"

def createProduct(request):
    form=ProductForm()
    if request.method =="POST":
        form=ProductForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form
    }
    return render(request,"ims/product.html",context)

def updateProduct(request,pk):
    prod_to_update=Product.objects.get(id=pk)
    form=ProductForm(instance=prod_to_update)
    if request.method == "POST":
        form=ProductForm(request.POST,instance=prod_to_update)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form
    }
    return render(request,"ims/product.html",context)

def deleteProduct(request,pk):
    prod_to_delete=Product.objects.get(id=pk)
    if request.method =="POST":
        prod_to_delete.delete()
        return redirect("/")
    context={
        "prod_to_delete":prod_to_delete
    }
    return render(request,"ims/deleteprod.html",context)

def specific_order(request,pk):
    # all_orders=Order.objects.all()
    one_order=Order.objects.get(id=pk)
    context={
        "oneorder":one_order
    }
    return render(request,"ims/orders.html",context)

def createOrder(request):
    form=OrderForm()
    if request.method =="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    }
    return render(request,"ims/neworder.html",context)

def updateOrder(request,pk):
    order_to_update=Order.objects.get(id=pk)
    form=OrderForm(instance=order_to_update)
    if request.method =="POST":
        form=OrderForm(request.POST,instance=order_to_update)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={
        "form":form
    }
    return render(request,"ims/neworder.html",context)

class OrderDetail(DetailView):
    model=Order
    template_name="ims/order_detail.html"

def deleteOrder(request,pk):
    order_to_delete=Order.objects.get(id=pk)
    if request.method =="POST":
        order_to_delete.delete()
        return redirect("/")

    context={
        "order_to_delete":order_to_delete
    }
    return render(request,"ims/deleteorder.html",context)