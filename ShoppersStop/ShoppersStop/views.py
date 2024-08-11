from django.shortcuts import render,redirect
from head.models import Product,Categories,Filter_Price,Color,Brand,Contact
from django.conf import settings
from django.core.mail import send_mail

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