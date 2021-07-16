from django.shortcuts import render
from .models import add_flight


def home(request):
    flights = add_flight.objects.all()
    title_contains = request.GET.get('local')
    title_exact = request.GET.get('id_exact')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    if title_contains != '' and title_contains is not None:
        flights = flights.filter(title__icontains=title_contains)
    if title_exact != '' and title_exact is not None:
        flights = flights.filter(title__icontains=title_exact)
    context = {
        'flights': flights,
    }

    return render(request, 'blogs/home.html', context)


def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})


def booking(request):
    return render(request, 'blogs/booking.html', {'title': 'Booking'})

# Create your views here.
