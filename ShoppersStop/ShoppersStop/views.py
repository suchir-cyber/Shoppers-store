from django.shortcuts import render,redirect
from head.models import Product,Categories,Filter_Price,Color,Brand,Contact
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

def BASE(request):
    return render(request,'Main/base.html')

def HOME(request):
    products = Product.objects.filter(status = 'Publish')
    context = {
        'products' : products
    }
    return render(request,'Main/index.html',context)

def PRODUCT(request):
    products = Product.objects.filter(status = 'Publish')
    categories = Categories.objects.all()
    prices = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('prices')
    COLOR_ID = request.GET.get('color')
    BRAND_ID = request.GET.get('brand')
    ATOZ_ID = request.GET.get('ATOZ')
    ZTOA_ID = request.GET.get('ZTOA')
    LowToHigh_ID = request.GET.get('LowToHigh')
    HighToLow_ID = request.GET.get('HighToLow')
    NEW_ID = request.GET.get('New')
    OLD_ID = request.GET.get('Old')


    if CATID:
        products = Product.objects.filter(categories = CATID,status = 'Publish')
    elif PRICE_FILTER_ID:
        products = Product.objects.filter(filter_price = PRICE_FILTER_ID,status = 'Publish')
    elif COLOR_ID:
        products = Product.objects.filter(color = COLOR_ID,status = 'Publish')
    elif BRAND_ID:
        products = Product.objects.filter(brand = BRAND_ID,status = 'Publish')
    elif ATOZ_ID:
        products = Product.objects.filter(status= 'Publish').order_by('name')  
    elif ZTOA_ID:
        products = Product.objects.filter(status= 'Publish').order_by('-name') 
    elif LowToHigh_ID:
        products = Product.objects.filter(status = 'Publish').order_by('price')    
    elif HighToLow_ID:
        products = Product.objects.filter(status = 'Publish').order_by('-price')
    elif NEW_ID:
        products = Product.objects.filter(condition = 'New',status = 'Publish').order_by('-id')
    elif OLD_ID:
        products = Product.objects.filter(condition = 'Old',status = 'Publish').order_by('-id')    
    else:
        products = Product.objects.filter(status = 'Publish').order_by('-id')


    context = {
        'products' : products,
        'categories' : categories,
        'prices' : prices,
        'color' : color,
        'brand' : brand
    }
    return render(request,'Main/product.html',context)


def SEARCH(request):
    query = request.GET.get('query')
    products = Product.objects.filter(name__icontains = query)

    context = {
        'products' : products
    }
    return render(request,'Main/search.html',context)


def PRODUCT_DETAIL_PAGE(request,id):
    prod = Product.objects.filter(id = id).first()
    context = {
        'prod' : prod
    }
    return render(request,'Main/product_single.html',context)

def Contact_Page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(
            name = name,
            email = email,
            subject = subject,
            message = message
        ) 
        
        subject = subject
        message = message
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from,['suchirpandula@gmail.com'])
            contact.save()
            return redirect('home')
        except:
            return redirect('contact')
        
    return render(request,'Main/contact.html')


def HandleRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.email = email
        customer.save()
        return redirect('register')
    return render(request,'Registration/auth.html')

def HandleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request,'Registration/auth.html')

def HandleLogout(request):
    logout(request)
    return redirect('home')


@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'Cart/cart_details.html')

def check_out(request):
    return render(request,'Cart/checkout.html')