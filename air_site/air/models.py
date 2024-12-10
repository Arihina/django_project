from django.db import models


class Passenger(models.Model):
    id = models.AutoField(primary_key=True, db_column='Идентификатор_пассажира')
    last_name = models.CharField(max_length=255, db_column='Фамилия_пассажира')
    first_name = models.CharField(max_length=255, db_column='Имя_пассажира')
    birth_date = models.DateField(db_column='Дата_рождения')
    gender = models.CharField(max_length=255, db_column='Пол_пассажира')
    passport_number = models.IntegerField(db_column='Номер_паспорта')
    contact_phone = models.CharField(max_length=255, db_column='Контактный_телефон')

    class Meta:
        db_table = 'Пассажир'


class Flight(models.Model):
    id = models.AutoField(primary_key=True, db_column='Идентификатор_рейса')
    flight_number = models.IntegerField(db_column='Номер_рейса')
    departure_date = models.DateField(db_column='Дата_вылета')
    departure_time = models.TimeField(db_column='Время_вылета')
    arrival_date = models.DateField(db_column='Дата_посадки')
    arrival_time = models.TimeField(db_column='Время_посадки')
    departure_airport = models.CharField(max_length=255, db_column='Аэропорт_вылета')
    arrival_airport = models.CharField(max_length=255, db_column='Аэропорт_посадки')

    class Meta:
        db_table = 'Рейс'


class Ticket(models.Model):
    id = models.AutoField(primary_key=True, db_column='Идентификатор_билета')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, db_column='Идентификатор_пассажира')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='Идентификатор_рейса')
    category = models.ForeignKey('TicketCategory', on_delete=models.CASCADE, db_column='Идентификатор_категории')
    price = models.DecimalField(max_digits=8, decimal_places=2, db_column='Стоимость_билета')
    service_class = models.CharField(max_length=255, db_column='Класс_обслуживания')

    class Meta:
        db_table = 'Билет'


class Airport(models.Model):
    id = models.AutoField(primary_key=True, db_column='Идентификатор_аэропорта')
    name = models.CharField(max_length=255, db_column='Название_аэропорта')
    city = models.CharField(max_length=255, db_column='Город_аэропорта')
    country = models.CharField(max_length=255, db_column='Страна_аэропорта')

    class Meta:
        db_table = 'Аэропорт'


class TicketCategory(models.Model):
    id = models.AutoField(primary_key=True, db_column='Идентификатор_категории')
    name = models.CharField(max_length=255, db_column='Название_категории')
    description = models.CharField(max_length=255, db_column='Описание_категории')
    additional_services = models.CharField(max_length=255, db_column='Дополниельные_услуги')

    class Meta:
        db_table = 'Категория_билета'


class Baggage(models.Model):
    id = models.AutoField(primary_key=True, db_column='Идентификатор_багажа')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, db_column='Идентификатор_пассажира')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='Идентификатор_рейса')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, db_column='Идентификатор_билета')
    category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE, db_column='Идентификатор_категории')
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, db_column='Идентификатор_аэропорта')
    weight = models.DecimalField(max_digits=8, decimal_places=2, db_column='Вес_багажа')
    size = models.CharField(max_length=255, db_column='Размер_багажа')
    content_description = models.CharField(max_length=255, db_column='Описание_содержимого')

    class Meta:
        db_table = 'Багаж'


class Airplane(models.Model):
    id = models.AutoField(primary_key=True, db_column='Идентификатор_самолета')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, db_column='Идентификатор_рейса')
    model = models.CharField(max_length=255, db_column='Модель_самолета')
    seat_count = models.IntegerField(db_column='Количество_мест')

    class Meta:
        db_table = 'Самолет'
