from django.db import models
from django.contrib.auth.models import User 


class FlightCompany(models.Model):
    """ Each flight company can include airports in different cities """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="companies")
    description = models.TextField()
    
    def __str__(self):
        return self.name


class AirLine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Airport(models.Model):
    city = models.CharField(max_length=255)
    image = models.ImageField(upload_to='city')
    company = models.ForeignKey(FlightCompany, on_delete=models.CASCADE, related_name="airports")    

    def __str__(self):
        return self.city
    
    class Meta:
        pass 
    
  
class Aircraft(models.Model):
    name = models.CharField(max_length=255)
    aircarft_type = models.CharField(max_length=255)
    image = models.ImageField(upload_to="air_craft")
    description = models.TextField()
    
    def __str__(self):
        return self.name 

    
class Flight(models.Model):
    flight_number = models.IntegerField()
    aircraft = models.OneToOneField(Aircraft, on_delete=models.CASCADE, related_name="flights")
    air_line = models.ForeignKey(AirLine, on_delete=models.CASCADE, related_name="flights")
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='tickets_origin')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='tickets_destination')
    cost = models.IntegerField(default=0)
    
    def __str__(self):
            return f"{self.flight_number}: {self.origin}-{self.destination}"
    
    def get_available_seat_number(self):
        # Get the highest seat number of existing tickets for this flight
        highest_seat_number = self.tickets.aggregate(models.Max('seat_number'))['seat_number__max']

        if highest_seat_number is None:
            return 1
        else:
            return highest_seat_number + 1
        
        
class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    passenger_phone = models.CharField(max_length=15)
    seat_number = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.passenger}"
    

class Store(models.Model):
    name = models.CharField(max_length=255)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="stores")
    store_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}: {self.airport}"


class Worker(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    image = models.ImageField(upload_to="workers")
    job = models.CharField(max_length=255)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="workers")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="workers")

    def __str__(self):
        return f"{self.name}, {self.job}"


