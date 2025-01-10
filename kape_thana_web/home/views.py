import time
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/index.html", {'timestamp': time.time()})

def contact_us(request):
    return render(request, "contact_us/contact_us.html", {'timestamp': time.time()})

def about_us(request):
    return render(request, "about_us/about_us.html", {'timestamp': time.time()})

def accomodation(request):
    return render(request, "accomodation/accomodation.html", {'timestamp': time.time()})

def news(request):
    return render(request, "news/news.html", {'timestamp': time.time()})