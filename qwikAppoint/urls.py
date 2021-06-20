from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from dashboard import views as d_views
from organization import views as o_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', d_views.homepage, name='home'),
    path('account/signup/', d_views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/', d_views.activate, name='activate'),
    path('organization/', include('organization.urls')),
    url(r'^create/profile/(?P<type>\w+)/$', d_views.create_profile,name='create_profile'),
    path('edit/<int:id>/', d_views.edit_profile, name='edit_profile'),
    url(r'^profile/(?P<username>\w+)/$', d_views.user_profile,name='profile'),
    path('org/list', o_views.org_list, name='org_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']