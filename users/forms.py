from django import forms
from django.forms import fields, models
from .models import UserProfile
from django.contrib.auth.models import User


# class UserForm(models.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('about', 'contact', 'location', 'birth_date')
