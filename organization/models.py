from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=15, blank=True)
    description = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=150, blank=True)


    def __str__(self):
        return self.user.username
