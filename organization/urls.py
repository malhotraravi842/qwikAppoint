from django.urls import path
from . import views

urlpatterns = [
    # path('', views.org_profile, name='org_profile'),
    # path('edit/', views.edit_org, name='edit_org'),
    path('appointment/<int:id>/', views.appointment, name='appointment'),
    # path('organizations/', views.orgs, name='orgs'),
]