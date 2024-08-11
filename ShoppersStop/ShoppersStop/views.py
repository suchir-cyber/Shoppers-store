from django.shortcuts import render,redirect
from head.models import Product,Categories,Filter_Price,Color,Brand

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

    if CATID:
        products = Product.objects.filter(categories = CATID,status = 'Publish')
    elif PRICE_FILTER_ID:
        products = Product.objects.filter(filter_price = PRICE_FILTER_ID,status = 'Publish')
    elif COLOR_ID:
        products = Product.objects.filter(color = COLOR_ID,status = 'Publish')
    else:
        products = Product.objects.filter(status = 'Publish')


    context = {
        'products' : products,
        'categories' : categories,
        'prices' : prices,
        'color' : color,
        'brand' : brand
    }
    return render(request,'Main/product.html',context)