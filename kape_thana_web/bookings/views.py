from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm
import time


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html', {'success': 'success'})
        else:
            return render(request, 'booking/booking.html', {'form': form, 'errors': form.errors})
    else:
        form = BookingForm()
    return render(request, 'booking/booking.html', {'form': form})

def terms_and_condition(request):
    return render(request, "terms_and_condition/terms_and_condition.html", {'timestamp': time.time()})
