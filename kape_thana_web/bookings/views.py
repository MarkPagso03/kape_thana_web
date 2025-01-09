from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm


import time

# Create your views here.
def booking(request):
    return render(request, "booking/booking.html", {'timestamp': time.time()})

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the data into the database
            return HttpResponse("Booking successfully saved!")
        else:
            return HttpResponse("Form data is invalid.")
    else:
        form = BookingForm()
    return render(request, "booking/booking.html", {'form': form})
