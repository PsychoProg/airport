from django import forms

class ReservationForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label='Phone Number')