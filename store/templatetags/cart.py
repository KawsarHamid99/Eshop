from django import template

register=template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return True
    return False



@register.filter(name="cart_quantity")
def cart_quantity(fm,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==fm.id:
            return cart.get(id)
    return False


#total price for specific product
@register.filter(name="Total_price")
def Total_price(fm,cart):
    return fm.price * cart_quantity(fm,cart)


# total Price for all product
@register.filter(name="Total_price_All")
def Total_price_All(fm,cart):
    sum=0
    for p in fm:
        sum +=Total_price(p,cart)
    return sum

@register.filter(name="TotalOrderPrice")
def TotalOrderPrice(price,quantity):
    return price*quantity