from django.shortcuts import render
from . import templates

def login(request):
    return render(request,'login.html')

def forgot_password(request):
    return render(request, 'forgot-pass.html')

def index(request):
    return render(request, 'index.html')

def inventory(request):
    return render(request, 'inventory.html')