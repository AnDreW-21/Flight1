from django.shortcuts import render
from .models import add_flight


def home(request):
    flights = add_flight.objects.all()
    context = {
        'flights': flights,
    }

    return render(request, 'blogs/home.html', context)


def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})


def booking(request):
    return render(request, 'blogs/booking.html', {'title': 'Booking'})

# Create your views here.
