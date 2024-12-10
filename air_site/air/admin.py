from django.contrib import admin

from .models import Passenger, Flight, Ticket, Airport, TicketCategory, Baggage, Airplane

admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Airport)
admin.site.register(TicketCategory)
admin.site.register(Baggage)
admin.site.register(Airplane)
