from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.views import LoginView

def register_page(request):
    return render(request, "register/register.html")

# def login_page(request):
#     return render(request, "register/login.html")


# register/views_html.py


class CustomLoginView(LoginView):
    template_name = 'register/login.html'

login_page = CustomLoginView.as_view()
