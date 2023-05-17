from django.contrib import admin

from ecommerceapp.models import CartModel, CategoryModel, OrderModel, ProductModel, customerModel

# Register your models here.
@admin.register(CategoryModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','category_name')

@admin.register(ProductModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','product_name','product_description','product_price','product_image','category')

@admin.register(customerModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','username','password','address','phone')

@admin.register(CartModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','product','customer')

@admin.register(OrderModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','product','customer')
