from django.forms import models
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.models import User
from dashboard.models import Profile
from django.views.generic import ListView
import json


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

def user_appointments(request):
    if request.user.is_authenticated:
        appointments = Appointment.objects.filter(user=request.user)

        return render(request, 'organization/user_appointments.html', {'appointments': appointments})
    else:
        return HttpResponseRedirect('/accounts/login/')

def take_appointment(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                user = request.user
                org_id = id
                org_name = Profile.objects.get(pk=id).full_name
                subject = form.cleaned_data['subject']
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']
                form_data = Appointment(user=user, org_id=org_id, org_name=org_name, subject=subject, date=date, time=time)
                form_data.save() 

                return HttpResponseRedirect('/organization/appointments/')

        form = AppointmentForm()
        return render(request, 'organization/take_appointment.html', {'form': form})
    else:
        return HttpResponseRedirect('/accounts/login/')

class OrganizationList(ListView):
    model = Profile
    template_name = 'organization/orgs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query_json"] = json.dumps(list(Profile.objects.values()))

        return context

        

# def orgs(request):
#     orgs = Profile.objects.filter(type='org')
#     return render(request, 'organization/orgs.html', {'orgs': orgs})