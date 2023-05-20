from django.urls import path  
from . import views    
app_name='demoapp' 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
]