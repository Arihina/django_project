from django import forms
from .models import Baggage, Passenger, Ticket, TicketCategory


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = [
            'last_name',
            'first_name',
            'birth_date',
            'gender',
            'passport_number',
            'contact_phone'
        ]
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'birth_date': 'Дата рождения',
            'gender': 'Пол',
            'passport_number': 'Номер паспорта',
            'contact_phone': 'Контактный телефон'
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=[('М', 'Мужчина'), ('Ж', 'Женщина')]),
            'contact_phone': forms.TextInput(attrs={'placeholder': 'Введите контактный телефон'}),
        }


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


class BaggageForm(forms.ModelForm):
    class Meta:
        model = Baggage
        fields = [
            'flight',
            'category',
            'airport',
            'weight',
            'size',
            'content_description'
        ]
        labels = {
            'flight': 'Рейс',
            'category': 'Категория',
            'airport': 'Аэропорт',
            'weight': 'Вес багажа (кг)',
            'size': 'Размер багажа',
            'content_description': 'Описание содержимого'
        }
        widgets = {
            'weight': forms.NumberInput(attrs={'step': '0.01'}),
            'size': forms.TextInput(attrs={'placeholder': 'Введите размер багажа'}),
            'content_description': forms.TextInput(attrs={'placeholder': 'Введите описание содержимого'}),
        }
