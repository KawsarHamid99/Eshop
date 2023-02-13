from django.contrib import admin
from .models.product import Product
from .models.catagory import Category
from .models.customer import Customer
from .models.orders import Order
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=["id","first_name","last_name","email","phone","password"]

    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name',"price","catagory","description","image"]

@admin.register(Order)
class ModelOrder(admin.ModelAdmin):
    list_display=["id","customer","product","quantity","price"]
