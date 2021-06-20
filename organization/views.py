from django.forms import models
from django.shortcuts import render, HttpResponseRedirect
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.models import User
from dashboard.models import Profile


def org_list(request):
    orgs = Profile.objects.filter(type='org')
    return render(request, 'organization/org_list.html', {'orgs': orgs})

def org_profile(request, username):
    try:
        user = User.objects.get(username=username)
        org = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        org = None
    
    return render(request, 'organization/org_profile.html', {'org': org})

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
        