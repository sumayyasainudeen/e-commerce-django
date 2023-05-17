from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=70)
    category_image= models.ImageField(upload_to="image/", null=True)

class ProductModel(models.Model):
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=70)
    product_description=models.CharField(max_length=220)
    product_price=models.IntegerField()   
    product_image= models.ImageField(upload_to="image/", null=True)

class customerModel(models.Model):
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)   
    username=models.CharField(max_length=70)
    password=models.CharField(max_length=70)
    address=models.CharField(max_length=220)
    phone=models.IntegerField()
 
class CartModel(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(customerModel,on_delete=models.CASCADE,null=True)

class OrderModel(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(customerModel,on_delete=models.CASCADE,null=True)