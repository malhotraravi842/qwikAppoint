from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.models import User
from dashboard.models import Profile
from django.core.mail import send_mail, BadHeaderError


def appointment_message(user, org, date, time):
    message = "Hello " + user + "\n" + "Your appointment is confirmed with " + org + " on " + str(date) + " at " + str(time)

    return message


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
                subject = "Appointment Confirmed"
                user = request.user
                org = User.objects.get(pk=id)
                org_name = Profile.objects.get(user=org).full_name
                sub = form.cleaned_data['subject']
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']
                email = user.email
                form_data = Appointment(user=user, org_id=id, org_name=org_name, subject=sub, date=date, time=time)
                form_data.save() 

                message = appointment_message(user.username, org_name, date, time)
                try:
                    send_mail(subject, message, 'rc069056@gmail.com', [email])
                except BadHeaderError:
                    return HttpResponse('Invalid')
                return HttpResponseRedirect('/organization/appointments/')

        form = AppointmentForm()
        return render(request, 'organization/take_appointment.html', {'form': form})
    else:
        return HttpResponseRedirect('/accounts/login/')
        