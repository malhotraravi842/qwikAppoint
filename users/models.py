from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    about = models.TextField(max_length=500, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
