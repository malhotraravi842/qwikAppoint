from django.db import models
from django.contrib.auth.models import User

USER_TYPE = (
    ("user", 'User'),
    ("org", 'Organization')
)

DEFAULT_IMAGE = 'images/default.svg'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=70, blank=False)
    image = models.ImageField(upload_to='media/profile', default=DEFAULT_IMAGE)
    type = models.CharField(max_length=20, choices=USER_TYPE, default="User", blank=False)
    contact = models.CharField(max_length=15, blank=False)
    bio = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=100, blank=False)
    pincode = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.user.username
