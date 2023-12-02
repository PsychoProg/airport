from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html', {})


def about_view(request):
    return render(request, 'about.html', {})


def reserve_view(request):
    return render(request, 'reservation.html', {})


def deals_view(request):
    return render(request, 'deals.html', {})