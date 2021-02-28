from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product
from .forms import *


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


def myform(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save()
            return render(request, 'single_product.html', {'product': new_product})
    else:
        form = ProductForm()
        return render(request, 'form.html', {'form': form})
