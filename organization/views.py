from django.forms import models
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.models import User
from dashboard.models import Profile


# def org_profile(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = OrganizationProfile(request.POST)
#             if form.is_valid():
#                 form.save()
#         else:
#             form = OrganizationProfile()
#         return render(request, 'organization/profile.html', {'form': form})
#     else:
#         return render(request, 'organization/profile.html', {'text': 'User is Not Logged In'})

# def edit_org(request):
#     profile = None
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = OrganizationProfile(request.POST)
#             if form.is_valid():
#                 contact = form.cleaned_data['contact']
#                 description = form.cleaned_data['description']
#                 address = form.cleaned_data['address']

#                 form_data = Organization(user=request.user, contact=contact, description=description, address=address)
#                 form_data.save()
#         else:
#             user = request.user
#             try:
#                 profile = Organization.objects.get(user=user)
#             except Organization.DoesNotExist:
#                 profile = None
#             form = OrganizationProfile(instance=profile)

#         return render(request, 'organization/edit_org.html', {'form': form, 'profile': profile})
#     else:
#         return render(request, 'organization/profile.html', {'text': 'User Not Logged In'})


def appointment(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                user = request.user
                org_id = id
                subject = form.cleaned_data['subject']
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']
                form_data = Appointment(user=user, org_id=org_id, subject=subject, date=date, time=time)
                form_data.save() 

        org = Profile.objects.get(pk=id)    
        form = AppointmentForm()
        appointments = Appointment.objects.filter(user=request.user)

        return render(request, 'organization/appointment.html', {'form': form, 'appointments': appointments, 'org':org})
    else:
        return redirect('/accounts/login/')


def orgs(request):
    orgs = Profile.objects.filter(type='org')
    return render(request, 'organization/orgs.html', {'orgs': orgs})