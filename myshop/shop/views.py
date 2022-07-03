from .models import Category, Product

import os

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import UserCreationForm 
from .forms import RegistrationForm,CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate,logout,login 
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from cloudipsp import Api, Checkout
from django.db.models import Max


def product_list(category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        return products.filter(category=category)
     


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     return render(request,
#                   'shop/product/detail.html',
#                   {'product': product})    
  

class IndexView(ListView):
    model = Product
    template_name = 'shop/index.html'


def Cars (request):

    category = get_object_or_404(Category, slug='pickup')
    
    object_list = Product.objects.filter(category=category)

    model = Product
    context = {}
    return render(request, 'shop/Cars.html', context)


class CarsView(ListView):
    
    category = get_object_or_404(Category, slug='passenger_car')
    

    productlist = Product.objects.filter(category=category)

    model = Product
    template_name = 'shop/Cars.html'    

class RegisterView(CreateView):
    template_name = 'shop/Reg.html'

class InfoView(ListView):
    model = Product
    template_name = 'shop/info.html'

class ContactsView(ListView):
    model = Product
    template_name = 'shop/contacts.html'

class TrucksView(ListView):
    category = get_object_or_404(Category, slug='pickup')

    productlist = Product.objects.filter(category=category)

    model = Product
    template_name = 'shop/Pickup_trucks.html'

class MinivansView(ListView):


    category = get_object_or_404(Category, slug='minivans')

    # productlist = Product.objects.filter(category=category)

    productlist = product_list('minivans')


    model = Product
    template_name = 'shop/Minivans.html'

class ApartsView(ListView):
    model = Product
    template_name = 'shop/Auto_parts.html'

class MpartsView(ListView):
    model = Product
    template_name = 'shop/Moto_parts.html'

class PaymentView(ListView):
    model = Product
    template_name = 'shop/Payment.html'

def registr(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт был создан для ' + user)

            return redirect('login')
    context = {'form':form}
    return render(request, 'shop/Reg.html', context)

def loginP(request):    
    template_name = 'shop/login.html'
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Логин ИЛИ Пароль были введены неправильно')

        context = {}
        return render(request, 'shop/login.html', context)

    
def logoutP(request):
    logout(request)
    return redirect('home')



def Payment(request, id):
    num = 0
    product = Product.objects.filter(id=id).aggregate(num=Max('price')).get(num)

    api = Api(merchant_id=1396424,
        secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "KZT",
        "amount": str(100000) + "00"
    }
    url = checkout.url(data).get('checkout_url')
    return (redirect(url))



def experimet(id):
    product = Product.objects.filter(id=id)
    return product