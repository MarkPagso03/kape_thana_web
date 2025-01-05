import time
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/index.html", {'timestamp': time.time()})

def contact_us(request):
    return render(request, "contact_us/contact_us.html", {'timestamp': time.time()})


def booking(request):
    return render(request, "booking/booking.html", {'timestamp': time.time()})

def about_us(request):
    return render(request, "about_us/about_us.html", {'timestamp': time.time()})