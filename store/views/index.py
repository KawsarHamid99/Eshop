from django.shortcuts import render
from store.models.product import Product
from store.models.catagory import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def Index(request):
    #request.session.clear()
    if request.method == "POST":
        product=request.POST.get("product")
        remove=request.POST.get("remove")
        print(f"--------------------------: {product}")
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session["cart"]=cart
        print(request.session['cart'])
    
    if request.method=="GET":
        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}


    data=Product.get_all_products()
    #data=Product.objects.all() 
    Product_category=request.GET.get('category')
    if Product_category:
        data=Product.get_all_products_by_ID(Product_category)
    print(request.session.get('email'))
    categories=Category.get_all_categories()
    return render(request,"store/index.html",{'data':data,"categories":categories})





