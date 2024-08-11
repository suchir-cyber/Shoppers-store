from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE, name = 'base'),
    path('',views.HOME,name = 'home'),
    path('products/',views.PRODUCT,name = 'products'),
    path('products/<str:id>',views.PRODUCT_DETAIL_PAGE,name = 'product_detail'),
    path('search/',views.SEARCH,name = 'search'),
    path('contact/',views.Contact_Page,name = 'contact')
] 

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
