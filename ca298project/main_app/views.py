from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Product, CaUser
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .permissions import admin_required


class CaUserSignupView(CreateView):
    model = CaUser
    form_class = CASignupForm
    template_name = "causer_signup.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class AdminSignupView(CreateView):
    model = CaUser
    form_class = AdminSignupForm
    template_name = "admin_signup.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


from django.contrib.auth.views import LoginView

class Login(LoginView):
    template_name = "login.html"

def logout_view(request):
    logout(request)
    return redirect('/')



def index(request):
    # return HttpResponse("Hello from main_app")
    return render(request, 'index.html')


def register(request):
    return HttpResponse("Hello from registration page")


def all_products(request):
    all_p = Product.objects.all()
    return render(request, 'all_products.html', {'products': all_p})


def singleproduct(request, prodid):
    prod = get_object_or_404(Product, pk=prodid)
    return render(request, 'single_product.html', {'product': prod})

@login_required
@admin_required
def myform(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            return render(request, 'single_product.html', {'product': new_product})
    else:
        form = ProductForm()
        return render(request, 'form.html', {'form': form})
