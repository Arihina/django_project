from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('flights/', views.flights, name='flights'),
    path('booking/', views.booking, name='booking'),
    path('search/', views.search, name='search'),
    path('aircraft/', views.aircraft, name='aircraft'),
]
