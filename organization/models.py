from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=15, blank=True)
    description = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=150, blank=True)


    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True, unique=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150, blank=True)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)

    def __str__(self):
        return self.appointment_id