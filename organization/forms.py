from django import forms
from .models import Organization
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

    