from django.shortcuts import render

def register_page(request):
    return render(request, "register/register.html")

def login_page(request):
    return render(request, "register/login.html")
