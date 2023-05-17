from ecommerceapp import views
from django.contrib import admin
from django.urls import  path


urlpatterns = [
    path('',views.index,name='index'),
    path('signin_page',views.signin_page,name='signin_page'),
    path('signin',views.signin,name='signin'),
    path('admin_home_page',views.admin_home_page,name='admin_home_page'),

    path('add_category_page',views.add_category_page,name='add_category_page'),
    path('add_category',views.add_category,name='add_category'),
    path('view_category',views.view_category,name='view_category'),
    path('edit_category_page/<int:pk>',views.edit_category_page,name='edit_category_page'),
    path('edit_category/<int:pk>',views.edit_category,name='edit_category'),
    path('delete_category/<int:pk>',views.delete_category,name='delete_category'),

    path('add_product_page',views.add_product_page,name='add_product_page'),
    path('add_product',views.add_product,name='add_product'),
    path('view_product',views.view_product,name='view_product'),
    path('edit_product_page/<int:pk>',views.edit_product_page,name='edit_product_page'),
    path('edit_product/<int:pk>',views.edit_product,name='edit_product'),
    path('delete_product/<int:pk>',views.delete_product,name='delete_product'),
    path('signout',views.signout,name='signout'),

    path('signup_page',views.signup_page,name='signup_page'),
    path('create_user',views.create_user,name='create_user'),
    path('view_profile',views.view_profile,name='view_profile'),

    path('category_page/<int:pk>',views.category_page,name='category_page'),
    path('more_products_page',views.more_products_page,name='more_products_page'),
    path('product_detail/<int:pk>',views.product_detail,name='product_detail'),


    path('add_cart/<int:pk>',views.add_cart,name='add_cart'),
    path('view_cart',views.view_cart,name='view_cart'),
    path('remove_cart/<int:pk>',views.remove_cart,name='remove_cart'),

    path('add_order/<int:pk>',views.add_order,name='add_order'),
    path('view_order',views.view_order,name='view_order'),
    path('view_users_page',views.view_users_page,name='view_users_page'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user'),


    path('edit_address_page',views.edit_address_page,name='edit_address_page'),
    path('edit_address/<int:pk>',views.edit_address,name='edit_address'),






   
]