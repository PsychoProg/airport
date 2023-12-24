from django.shortcuts import redirect, render
from .models import AirLine, Aircraft, Flight, FlightCompany, Ticket, Airport, Worker
from django.views.generic import ListView
from django.views.generic import DetailView


def home_view(request):
    flights = Flight.objects.all()[:3]
    context = {
        'title': 'home',
        'flights': flights,
    }    
    return render(request, 'index.html', context)


def about_view(request):
    context = {
        'title': 'about'
    }
    return render(request, 'about.html', context)


def deals_view(request):
    deals = Flight.objects.all()
    context = {
        'title': 'deals',
        'deals': deals,
    }
    return render(request, 'deals.html', context)


def reserve_view(request, flight_id):
    context = {
        'title': 'reservations',
    }
    if request.user.is_authenticated:
        flight = Flight.objects.get(pk=flight_id)
        cost = flight.cost
        seat_number = flight.get_available_seat_number()

        if request.method == "POST":
            phone = request.POST.get('Number')
            
            Ticket.objects.create(
                flight=flight, 
                passenger=request.user, 
                passenger_phone=phone,
                seat_number=seat_number,
                cost=int(cost))
            
        context = {
            "flight": flight,
            "user": request.user.username,
        }
        
    return render(request, 'reservation.html', context)


def services(request):
    airports = Airport.objects.all()
    companies = FlightCompany.objects.all()
    airlines = AirLine.objects.all()
    context = {
        'title': 'services',
        'airports': airports,
        'companies': companies,
        'airlines': airlines,
    }
    return render(request, 'services.html', context)



class FlightCompanyDetailView(DetailView):
    model = FlightCompany
    template_name = 'flight_company_detail.html'
    context_object_name = 'company'
    
    


class AircraftDetailView(DetailView):
    model = Aircraft
    template_name = 'aircraft_detail.html'
    context_object_name = 'aircraft'

class WorkerListView(ListView):
    model = Worker
    template_name = 'worker_list.html'
    context_object_name = 'workers'