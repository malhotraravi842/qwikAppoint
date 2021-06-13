from django import forms
from django.db.models import fields
from django.forms.models import model_to_dict
from .models import Organization, Appointment
from django.contrib.auth.models import User

class OrganizationProfile(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ('contact', 'description', 'address')
        widgets = {
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

    

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('subject', 'date', 'time')
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }