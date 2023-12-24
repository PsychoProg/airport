from django.contrib import admin
from . import models 

admin.site.register(models.FlightCompany)
admin.site.register(models.AirLine)
admin.site.register(models.Airport)
admin.site.register(models.Aircraft)
admin.site.register(models.Flight)
admin.site.register(models.Ticket)
admin.site.register(models.Store)
admin.site.register(models.Worker)

