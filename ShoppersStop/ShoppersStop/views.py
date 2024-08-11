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

    if CATID:
        products = Product.objects.filter(categories = CATID)
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