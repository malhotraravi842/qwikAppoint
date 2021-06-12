from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from dashboard import views as d_views
# from dashboard.forms import UserLoginForm
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', d_views.homepage, name='home'),
    path('account/signup/', d_views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/', d_views.activate, name='activate'),
    path('organization/', include('organization.urls')),
    path('user/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
