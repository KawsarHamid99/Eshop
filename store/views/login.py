from django.shortcuts import render
from store.models.product import Product
from store.models.catagory import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password

def loginForm(request):
    if request.method=="GET":
        return render(request,"authentication/login.html")
    else:
        email=request.POST.get("email")
        password=request.POST.get("password")
        customer=Customer.get_customer_by_email(email)

        error_massage=None
        if customer is not None:
            flag=check_password(password,customer.password)
            print(flag)
            if flag:
                error_massage="password is corrected" 
                request.session['customer_id']=customer.id
                request.session['email']=customer.email
            else:
                error_massage="password is not correct"

        else:
            error_massage="customer is not found"

        return render(request,"authentication/login.html",{"error":error_massage})




