from django.contrib import admin
from .models import Organization, Appointment

# Register your models here.
admin.site.register(Organization)
admin.site.register(Appointment)