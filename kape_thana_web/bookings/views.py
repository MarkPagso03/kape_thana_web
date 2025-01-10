from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .forms import BookingForm
from django.contrib import messages
import time
from pytz import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden


def current_time_utc_plus_8():
    local_timezone = timezone('Asia/Singapore')
    local_time = now().astimezone(local_timezone)
    clean_local_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
    print(clean_local_time)
    return clean_local_time


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)

            # Set the `created_at` field manually
            booking_instance.created_at = current_time_utc_plus_8()

            # Save the instance to the database
            booking_instance.save()

            fb_username = form.cleaned_data.get('fb_username')
            return render(request, 'home/index.html', {'success': 'success', 'fb_username': fb_username})
        else:
            return render(request, 'booking/booking.html', {'form': form, 'errors': form.errors})
    else:
        form = BookingForm()
    return render(request, 'booking/booking.html', {'form': form})

def terms_and_condition(request):
    return render(request, "terms_and_condition/terms_and_condition.html", {'timestamp': time.time()})



class InQueueListView(APIView):
    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(accepted=0).order_by('created_at')
        print(bookings)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)  # Always returns JSON

class AcceptedListView(APIView):
    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(accepted=1).order_by('created_at')
        print(bookings)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)  # Always returns JSON

class OnGoingListView(APIView):
    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(accepted=2).order_by('created_at')
        print(bookings)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)  # Always returns JSON

class HistoryListView(APIView):
    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(accepted=3).order_by('-created_at')
        print(bookings)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)  # Always returns JSON


@staff_member_required
def dashboard(request):
    return render(request, "staff_dashboard/dashboard.html", {'timestamp': time.time()})


@csrf_exempt
@api_view(['POST'])
def update_or_delete_booking(request):
    try:
        booking_id = request.data.get('id')
        action = request.data.get('action')  # Either 'accept' or 'reject'

        if action == 'accept':
            # Update the `accepted` field to 1
            booking = Booking.objects.get(id=booking_id)
            booking.accepted += 1
            booking.save()
            return JsonResponse({'success': True, 'message': 'Booking accepted!'})

        elif action == 'reject':
            # Delete the booking
            booking = Booking.objects.get(id=booking_id)
            booking.delete()
            return JsonResponse({'success': True, 'message': 'Booking rejected and deleted!'})

        else:
            return JsonResponse({'success': False, 'message': 'Invalid action!'}, status=400)

    except Booking.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Booking not found!'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@staff_member_required
def history(request):
    return render(request, "history/history.html", {'timestamp': time.time()})
