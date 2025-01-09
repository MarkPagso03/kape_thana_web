from django.db import models

# Create your models here.
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"