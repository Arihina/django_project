from django.shortcuts import HttpResponse, render

from .models import Airplane, Flight


def index(request):
    return render(request, 'index.html')


def flights(request):
    flights = Flight.objects.all()
    return render(request, 'flights.html', {'flights': flights})


def booking(request):
    return HttpResponse('booking')


def search(request):
    return HttpResponse('search')


def aircraft(request):
    airplanes = Airplane.objects.all()
    return render(request, 'aircraft.html', {'airplanes': airplanes})
