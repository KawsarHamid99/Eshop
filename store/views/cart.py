from django.shortcuts import render
from store.models.product import Product
def cart_view(request):
    cart=request.session.get('cart',None)
    if cart:
        ids=list(cart.keys())
    #product=Product.objects.filter(id__in=ids)
        product=Product.get_product_by_id(ids)
    else:
        product=None

    return render(request,"store/cart.html",{'products':product})