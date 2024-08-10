from django.urls import path
from head.views import index

urlpatterns = [
    path('',index)
]
