from django.shortcuts import HttpResponse, render

from .models import Airplane


def index(request):
    return render(request, 'index.html')


def flights(request):
    return HttpResponse('flights')


def booking(request):
    return HttpResponse('booking')


def search(request):
    return HttpResponse('search')


def aircraft(request):
    airplanes = Airplane.objects.all()
    return render(request, 'aircraft.html', {'airplanes': airplanes})
