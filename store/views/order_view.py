from django.views import View
from django.shortcuts import render
from store.models import Order

from store.middlewares.auth import Auth_middleware
from django.utils.decorators import method_decorator


class OrderView(View):
    @method_decorator(Auth_middleware)
    def get(self,request):
        customer=request.session.get("customer_id")
        orders=Order.get_order_by_customer(customer)
        print(orders)
        orders=orders.reverse()
        print(orders) 
        return render(request,"store/orders.html",{"products":orders})