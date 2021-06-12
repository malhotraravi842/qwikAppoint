from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('contact','birth_date', 'location', 'about')
        widgets = {
            'contact' : forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date' : forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'location' : forms.TextInput(attrs={'class': 'form-control'}),
            'about' : forms.TextInput(attrs={'class': 'form-control'}),
        }
