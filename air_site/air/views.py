from django.shortcuts import render

from .forms import FlightSearchForm, BaggageForm, PassengerForm
from .models import Airplane, Flight, Ticket


def index(request):
    return render(request, 'index.html')


def flights(request):
    flights = Flight.objects.all()
    return render(request, 'flights.html', {'flights': flights})


def booking(request):
    if request.method == 'POST':
        passenger_form = PassengerForm(request.POST)
        baggage_form = BaggageForm(request.POST)

        if passenger_form.is_valid() and baggage_form.is_valid():
            passenger = passenger_form.save()
            baggage = baggage_form.save(commit=False)
            baggage.passenger = passenger
            weight = baggage.weight

            ticket_price = weight * 1000

            ticket = Ticket.objects.create(
                passenger=passenger,
                flight=baggage.flight,
                category=baggage.category,
                price=ticket_price,
            )

            baggage.ticket = ticket
            baggage.save()

            request.session['ticket'] = {
                'id': ticket.id,
                'passenger': str(ticket.passenger),
                'flight': str(ticket.flight),
                'category': str(ticket.category),
                'price': str(ticket.price),
            }


    else:
        passenger_form = PassengerForm()
        baggage_form = BaggageForm()

    return render(request, 'baggage_form.html', {
        'passenger_form': passenger_form,
        'baggage_form': baggage_form,
    })


def search(request):
    form = FlightSearchForm(request.GET or None)
    flights = Flight.objects.all()

    if form.is_valid():
        flight_number = form.cleaned_data.get('flight_number')
        departure_airport = form.cleaned_data.get('departure_airport')
        arrival_airport = form.cleaned_data.get('arrival_airport')
        departure_date = form.cleaned_data.get('departure_date')
        arrival_date = form.cleaned_data.get('arrival_date')
        departure_time = form.cleaned_data.get('departure_time')
        arrival_time = form.cleaned_data.get('arrival_time')

        if flight_number:
            flights = flights.filter(flight_number__icontains=flight_number)
        if departure_airport:
            flights = flights.filter(departure_airport__icontains=departure_airport)
        if arrival_airport:
            flights = flights.filter(arrival_airport__icontains=arrival_airport)
        if departure_date:
            flights = flights.filter(departure_date=departure_date)
        if arrival_date:
            flights = flights.filter(arrival_date=arrival_date)
        if departure_time:
            flights = flights.filter(departure_time=departure_time)
        if arrival_time:
            flights = flights.filter(arrival_time=arrival_time)

    return render(request, 'flights_search.html', {'flights': flights, 'form': form})


def aircraft(request):
    airplanes = Airplane.objects.all()
    return render(request, 'aircraft.html', {'airplanes': airplanes})
