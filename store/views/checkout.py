from django.views import View
from django.shortcuts import render,HttpResponseRedirect
from store.models import Product
from store.models import Order,Customer
class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get("phone")
        customer=request.session.get('customer_id',None)
        cart=request.session.get('cart',None)
        products=Product.get_product_by_id(list(cart.keys()))
        #print(products)
        #print(cart)
        for product in products:
            #print(product,customer,cart.get(str(product.id)),product.id,product.price,address)
            order=Order(
            product=product,
            customer=Customer(id=customer),
            quantity=cart.get(str(product.id)),
            price=product.price,
            address=address, 
            phone=phone)
            order.save()
        request.session['cart']={}
    
        return HttpResponseRedirect("/cart/")