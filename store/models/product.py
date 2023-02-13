from django.db import models
from .catagory import Category
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    catagory=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default="",null=True,blank=True)
    image=models.ImageField(upload_to='uploads/products/')


    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_ID(cat_id):
        if cat_id:
            return Product.objects.filter(catagory=cat_id)
        else:
            return Product.objects.all()


    @staticmethod
    def get_product_by_id(ids):
        qs=Product.objects.filter(id__in = ids)
        return qs

    def __str__(self):
        return str(self.name)