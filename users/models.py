from django.db import models
from django.contrib.auth.models import User
# from tinymce.models import HTMLField
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=15)
    dob = models.DateField()

    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            
    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
