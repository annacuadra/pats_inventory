from django.contrib import admin
from django.urls import path
from setup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot-pass'),
    path('home/', views.index, name='index'),
    path('inventory/', views.inventory, name='inventory'),
]
