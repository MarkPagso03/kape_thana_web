from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .forms import BookingForm
from django.contrib import messages
import time


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

            fb_username = form.cleaned_data.get('fb_username')
            return render(request, 'home/index.html', {'success': 'success', 'fb_username': fb_username})
        else:
            return render(request, 'booking/booking.html', {'form': form, 'errors': form.errors})
    else:
        form = BookingForm()
    return render(request, 'booking/booking.html', {'form': form})

def terms_and_condition(request):
    return render(request, "terms_and_condition/terms_and_condition.html", {'timestamp': time.time()})
