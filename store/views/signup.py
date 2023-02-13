from django.shortcuts import render
from store.models.product import Product
from store.models.catagory import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password


def Signup(request):
    error_massege=""
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        contactnumber=request.POST.get('contactnumber')
        email=request.POST.get('email')
        password=request.POST.get('password')
        error_massege=[]
        isExist=Customer.objects.filter(email=email)
        if isExist:
            error_massege="Email Address Already Exist..."
        else:
            password=make_password(password)

            customer=Customer(first_name=firstname,last_name=lastname,phone=contactnumber,email=email,password=password)
            customer.save() 
    return render(request,"authentication/signup.html",{"error_message":error_massege})

