from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ecommerceapp.models import CartModel, CategoryModel, OrderModel, ProductModel, customerModel
from django.db.models import Count



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        current_user = request.user
        cust_id=current_user.id-1   
        product=ProductModel.objects.all().order_by('-id')
        category=CategoryModel.objects.all()
        c_number = CartModel.objects.filter(customer=cust_id).count()
        o_number = OrderModel.objects.filter(customer=cust_id).count()
        return render(request,'index.html',{'product':product,'category':category,'no':c_number,'o_no':o_number})
    else:
        product=ProductModel.objects.all().order_by('-id')
        category=CategoryModel.objects.all()
        
        return render(request,'index.html',{'product':product,'category':category})
# def index(request):
#     current_user = request.user
#     cust_id=current_user.id-1   
#     product=ProductModel.objects.all().order_by('-id')
#     category=CategoryModel.objects.all()
#     c_number = CartModel.objects.filter(customer=cust_id).count()
#     o_number = OrderModel.objects.filter(customer=cust_id).count()
#     return render(request,'index.html',{'product':product,'category':category,'no':c_number,'o_no':o_number})



def signin_page(request):
     return render(request,'signin.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_home_page')
            else:
                login(request, user)
                auth.login(request, user)
                # messages.success(request,' Welcome...'+ user.first_name)
                return redirect('index')
        else:
            messages.info(request,'Please Register First!')
            return redirect('signin_page')
    return redirect('signin_page')

def admin_home_page(request):
    return render(request,'admin/adminhome.html')


def add_category_page(request):
    return render(request,'admin/addcategory.html')

def add_category(request):
     if request.method == 'POST':
        cname = request.POST['categoryname']
        image = request.FILES.get('file')
        data = CategoryModel(category_name=cname,category_image=image)
        data.save()
        messages.success(request,'Category Added')
        return redirect('add_category_page')

def view_category(request):
    category = CategoryModel.objects.all()
    return render(request,'admin/showcategory.html',{'category':category})

def edit_category_page(request,pk):
    category = CategoryModel.objects.get(id=pk)
    return render(request,'admin/editcategory.html',{'category':category})

def edit_category(request,pk):
    if request.method == 'POST':
        category = CategoryModel.objects.get(id=pk)
        category.category_name= request.POST['categoryname']  

        old=category.category_image
        new=request.FILES.get('file')
        if old != None and new == None:
            category.category_image=old
        else:
            category.category_image=new

        category.save()
        return redirect ('view_category')

def delete_category(request,pk):
    category = CategoryModel.objects.get(id=pk)
    category.delete()
    return redirect('view_category')


def add_product_page(request):
    category=CategoryModel.objects.all()
    return render(request,'admin/addproduct.html',{'category':category})

def add_product(request):
      if request.method == 'POST':
        select = request.POST['select']
        category = CategoryModel.objects.get(id=select)
        # cname=category.category_name
        pname = request.POST['productname']
        desc = request.POST['productdescription']
        price = request.POST['Productprice']
        image = request.FILES.get('file')
        data = ProductModel(product_name=pname,product_description=desc,product_price=price,product_image=image,category=category)
        data.save()
        messages.success(request,'Product Added')
        return redirect('add_product_page')

def view_product(request):
    product = ProductModel.objects.all()
    return render(request,'admin/showproduct.html',{'product':product})

def edit_product_page(request,pk):
    product = ProductModel.objects.get(id=pk)
    category=CategoryModel.objects.all()
    return render(request,'admin/editproduct.html',{'product':product,'category':category})

def edit_product(request,pk):
    if request.method == 'POST':
        product = ProductModel.objects.get(id=pk)
        product.product_name= request.POST['productname']  
        product.product_description= request.POST['productdescription']
        product.product_price= request.POST['Productprice']
        select = request.POST['select']
        category = CategoryModel.objects.get(id=select)
        product.category = category
        
        old=product.product_image
        new=request.FILES.get('file')
        if old != None and new == None:
            product.product_image=old
        else:
            product.product_image=new

        product.save()
        return redirect ('view_product')

def delete_product(request,pk):
    product = ProductModel.objects.get(id=pk)
    product.delete()
    return redirect('view_product')

def signout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('index')


def signup_page(request):
    return render(request,'user/signup.html')

def create_user(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        uname = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        add = request.POST['address']
        ph = request.POST['phone_number']

        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'This Username Already Exists!')
                return redirect('signup_page')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This Email Already Exists!')
                return redirect('signup_page')
            else:
                user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=password)
                user.save()

                data = User.objects.get(id=user.id)
                customer = customerModel(first_name=fname,last_name=lname,email=email,username=uname,password=password,address=add,phone=ph)
                customer.save()
                messages.success(request,' Welcome...'+ data.first_name)
                return redirect('signin_page')
        else:
            messages.info(request,'Password is not Matching!')
            return redirect('signup_page')
    else:
        return redirect('signup_page')

def category_page(request,pk):
   
    cats= CategoryModel.objects.all()
    cat= CategoryModel.objects.get(id=pk)
    product= ProductModel.objects.filter(category=cat).order_by('-id')
   
    return render(request,'category.html',{'product':product,'cat':cat,'cats':cats})


def category_page1(request,pk):
    
    category= CategoryModel.objects.all()
    return render(request,'category.html',{'cat':category})

def more_products_page(request):
   
    product=ProductModel.objects.all().order_by('-id')
    category=CategoryModel.objects.all()
    return render(request,'moreproducts.html',{'product':product,'category':category})

def product_detail(request,pk):
   
    product =ProductModel.objects.filter(id=pk)
    return render(request,'productdetails.html',{'product':product})

@login_required(login_url='signin_page')
def add_cart(request,pk):
    current_user = request.user
    cust_id=current_user.id-1
    customer = customerModel.objects.get(id=cust_id)
    product = ProductModel.objects.get(id=pk)
    # p_count = CartModel.objects.filter(product=product, customer=customer).count()
   
    try:
        cart_product = CartModel.objects.get(product=product, customer=customer)
        p_count = cart_product.quantity
    except CartModel.DoesNotExist:
        p_count = 0
    # p_count = products.quantity
   
    qty = int(p_count)+1
    
    if p_count == 0:
        cart= CartModel(product=product,customer=customer,quantity=qty)
        cart.save()
    else:
        cart = CartModel.objects.get(product=product,customer=customer)
        cart.quantity=qty
        cart.save()
    return redirect('/')

@login_required(login_url='signin_page')
def view_cart(request):
    current_user = request.user
    cust_id=current_user.id-1
    print(cust_id)
    customer=customerModel.objects.filter(id=cust_id)
    c_number = CartModel.objects.filter(customer=cust_id).count()
    cart = CartModel.objects.filter(customer=cust_id)
    o_number = OrderModel.objects.filter(customer=cust_id).count()
    return render(request,'user/cart.html',{'cart':cart,'no':c_number,'o_no':o_number})

def remove_cart(request,pk):
    cart=CartModel.objects.get(id=pk)
    cart.delete()
    return redirect('view_cart')

@login_required(login_url='signin_page')
def add_order(request,pk):
    product = ProductModel.objects.get(id=pk)
    current_user = request.user
    cust_id=current_user.id-1
    customer = customerModel.objects.get(id=cust_id)
    
    # order_product = OrderModel.objects.get(product=product,customer=customer)
    # p_count = order_product.quantity
    try:
        order_product = OrderModel.objects.get(product=product, customer=customer)
        o_count = order_product.quantity
    except OrderModel.DoesNotExist:
        o_count = 0

    qty = o_count+1
    
    if o_count == 0:
        order= OrderModel(product=product,customer=customer,quantity=qty)
        order.save()
    else:
        order = OrderModel.objects.get(product=product,customer=customer)
        order.quantity=qty
        order.save()
    return redirect('/')

@login_required(login_url='signin_page')
def view_order(request):
    current_user = request.user
    cust_id=current_user.id-1
    print(cust_id)
    c_number = CartModel.objects.filter(customer=cust_id).count()
    o_number = OrderModel.objects.filter(customer=cust_id).count()
    customer=customerModel.objects.filter(id=cust_id)
    order = OrderModel.objects.filter(customer=cust_id)
    return render(request,'user/myorders.html',{'order':order,'no':c_number,'o_no':o_number})


@login_required(login_url='signin_page')
def view_profile(request):
    current_user = request.user
    cust_id=current_user.id-1
    customer = customerModel.objects.filter(id=cust_id)
    c_number = CartModel.objects.filter(customer=cust_id).count()
    o_number = OrderModel.objects.filter(customer=cust_id).count()
    return render(request,'user/profile.html',{'customer':customer,'no':c_number,'o_no':o_number})

def view_users_page(request):
    customers = customerModel.objects.all()
    return render(request,'admin/viewusers.html',{'customers':customers})

def delete_user(request,pk):
    customer=customerModel.objects.get(id=pk)
    customer.delete()
    return redirect('view_users_page')

@login_required(login_url='signin_page')
def edit_address_page(request):
    current_user = request.user
    cust_id=current_user.id-1
    customer = customerModel.objects.get(id=cust_id)
    return render(request,'user/editaddress.html',{'customer':customer})

def edit_address(request,pk):
    if request.method == 'POST':
        customer = customerModel.objects.get(id=pk)
        customer.address= request.POST['address']  
        customer.save()
        return redirect ('view_profile')
















# https://www.youtube.com/watch?v=h4A6a_6ogjE
# https://www.youtube.com/watch?v=jU9EL3bSC2s








