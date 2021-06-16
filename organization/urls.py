from django.urls import path
from . import views

urlpatterns = [
    path('appointment/<int:id>/', views.take_appointment, name='appointment'),
    path('appointments/', views.user_appointments, name='user_appointments'),
]