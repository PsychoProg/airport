from django.contrib import admin
from . import models 

admin.site.register(models.Airport)
admin.site.register(models.Flight)
admin.site.register(models.Ticket)
