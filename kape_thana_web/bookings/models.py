from django.db import models
from django.utils.timezone import now
from pytz import timezone


def current_time_utc_plus_8():
    local_timezone = timezone('Asia/Singapore')
    local_time = now().astimezone(local_timezone)
    clean_local_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
    print(clean_local_time)
    return clean_local_time



class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    fb_username = models.CharField(max_length=100, null=True)
    check_in = models.DateField()
    check_out = models.DateField(null=True, blank=True)  # Temporarily allow NULL
    guests = models.PositiveIntegerField()
    accepted = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_at = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.full_name} - Time {self.created_at}"
