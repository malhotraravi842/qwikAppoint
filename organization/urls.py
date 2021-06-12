from django.urls import path
from . import views

urlpatterns = [
    path('', views.org_profile, name='org_profile'),
]