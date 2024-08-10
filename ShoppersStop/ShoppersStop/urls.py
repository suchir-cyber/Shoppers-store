from django.contrib import admin
from django.urls import path,include
from head.views import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('head.urls'))
]
