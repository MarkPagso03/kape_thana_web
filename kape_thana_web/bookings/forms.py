from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'mobile_number', 'email', 'fb_username', 'check_in', 'check_out', 'guests', 'room_no', 'accepted']

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_out and check_in and check_out <= check_in:
            self.add_error('check_out', "Check-out date must be after the check-in date.")

        return cleaned_data
