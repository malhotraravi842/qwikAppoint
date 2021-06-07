from django.contrib import admin
from django.urls import path, include
from dashboard import views as d_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', d_views.homepage, name='home'),
    path('organization/', include('organization.urls')),
    path('user/', include('users.urls')),
]
