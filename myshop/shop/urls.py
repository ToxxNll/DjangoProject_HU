from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from .views import (IndexView, CarsView, RegisterView, InfoView, ContactsView, TrucksView, MinivansView, ApartsView,
                    MpartsView, PaymentView)
from shop import views

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('reg/', views.registr , name = 'reg'),
    path('login/', views.loginP, name="login"),
    path('logout/', views.logoutP, name="logout"),
    path('info/', InfoView.as_view(), name="info"),
    path('contacts/', ContactsView.as_view(), name="contacts"),
    path('trucks/', TrucksView.as_view(), name="trucks"),
    path('minivans/', MinivansView.as_view(), name="minivans"),
    path('auto_parts/', ApartsView.as_view(), name="auto_parts"),
    path('moto_parts/', MpartsView.as_view(), name="moto_parts"),
    path('payment/<int:id>/', views.Payment, name="payment"),
]