from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('flights/', views.flights, name='flights'),
    path('booking/', views.booking, name='booking'),
    path('search/', views.search, name='search'),
    path('aircraft/', views.aircraft, name='aircraft'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
]
