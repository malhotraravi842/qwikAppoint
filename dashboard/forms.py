from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


USER_TYPE = (
    ("user", 'User'),
    ("org", 'Organization')
)


def validate_email_unique(value):
    exists = User.objects.filter(email=value)
    if exists:
        raise ValidationError("Email address %s already exists." % value)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True, validators=[validate_email_unique], help_text='Required', label='Email Address')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name','type', 'contact', 'bio', 'address', 'pincode')

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'type' : forms.Select(choices=USER_TYPE, attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name','contact', 'bio', 'address', 'pincode')

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
        }
