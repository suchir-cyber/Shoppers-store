from django.shortcuts import render,redirect
from head.models import Product

def BASE(request):
    return render(request,'Main/base.html')

def HOME(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request,'Main/index.html',context)