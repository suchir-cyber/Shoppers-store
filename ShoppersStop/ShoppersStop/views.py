from django.shortcuts import render,redirect

def BASE(request):
    return render(request,'Main/base.html')