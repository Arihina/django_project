from django.shortcuts import render, redirect

from .forms import FlightSearchForm, BaggageForm, PassengerForm, LoginForm, BookingForm
from .models import Airplane, Flight, Ticket, Passenger


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

            ticket_price = 5000 + weight * 1000

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


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            passport_number = form.cleaned_data['passport_number']
            try:
                passenger = Passenger.objects.get(passport_number=passport_number)
                request.session['passenger_id'] = passenger.id
                return redirect('profile')
            except Passenger.DoesNotExist:
                form.add_error('passport_number', 'Пассажир с таким номером паспорта не найден.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def profile(request):
    if 'passenger_id' not in request.session:
        return redirect('login')

    passenger = Passenger.objects.get(id=request.session['passenger_id'])
    tickets = Ticket.objects.filter(passenger=passenger)

    search_query = request.GET.get('search')
    if search_query:
        tickets = tickets.filter(flight__flight_number__icontains=search_query)

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            baggage = booking_form.save(commit=False)
            baggage.passenger = passenger
            weight = baggage.weight

            ticket_price = 5000 + weight * 1000

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
            return redirect('profile')
    else:
        booking_form = BookingForm()

    return render(request, 'profile.html', {
        'passenger': passenger,
        'tickets': tickets,
        'booking_form': booking_form,
    })


def logout(request):
    request.session.flush()
    return redirect('login')


def registration(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PassengerForm()
    return render(request, 'register.html', {'form': form})
