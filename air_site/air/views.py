from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, 'index.html')


def flights(request):
    return HttpResponse('flights')


def booking(request):
    return HttpResponse('booking')


def search(request):
    return HttpResponse('search')


def aircraft(request):
    return HttpResponse('aircraft')
