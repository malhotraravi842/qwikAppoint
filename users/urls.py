from  django.urls import path
from  . import views


urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
]