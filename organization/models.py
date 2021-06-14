from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Profile


class Appointment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org_id = models.IntegerField(blank=False)
    subject = models.CharField(max_length=150, blank=True)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)

    def __str__(self):
        return self.user.username