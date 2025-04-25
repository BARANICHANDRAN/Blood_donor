from django import forms
from django.core.exceptions import ValidationError
from datetime import date
import re 
from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        widgets = {
            'last_donated': forms.DateInput(attrs={'type': 'date'})  # Date picker for last_donated
        }

    def clean_last_donated(self):
        last_donated = self.cleaned_data.get('last_donated')
        if last_donated and last_donated > date.today():  # Ensure the date is in the past
            raise ValidationError("The last donated date must be in the past.")
        return last_donated

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if contact and not re.match(r'^\d{10}$', contact):  # Match exactly 10 digits
            raise ValidationError("Phone number must be 10 digits long.")
        return contact
