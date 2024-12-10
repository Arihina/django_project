from django import forms


class FlightSearchForm(forms.Form):
    flight_number = forms.CharField(required=False, label='Номер Рейса')
    departure_airport = forms.CharField(required=False, label='Аэропорт Вылета')
    arrival_airport = forms.CharField(required=False, label='Аэропорт Посадки')
    departure_date = forms.DateField(required=False, label='Дата Вылета',
                                     widget=forms.TextInput(attrs={'type': 'date'}))
    arrival_date = forms.DateField(required=False, label='Дата Посадки', widget=forms.TextInput(attrs={'type': 'date'}))
    departure_time = forms.TimeField(required=False, label='Время Вылета',
                                     widget=forms.TextInput(attrs={'type': 'time'}))
    arrival_time = forms.TimeField(required=False, label='Время Посадки',
                                   widget=forms.TextInput(attrs={'type': 'time'}))
