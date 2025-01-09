from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    fb_username = models.CharField(max_length=100, null=True)
    check_in = models.DateField()
    check_out = models.DateField(null=True, blank=True)  # Temporarily allow NULL
    guests = models.PositiveIntegerField()
    room_no = models.PositiveIntegerField(null=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - Room {self.room_no}"
