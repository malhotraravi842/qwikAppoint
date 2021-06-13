from django.shortcuts import render
from .forms import OrganizationProfile, AppointmentForm
from .models import Appointment, Organization


def org_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrganizationProfile(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = OrganizationProfile()
        return render(request, 'organization/profile.html', {'form': form})
    else:
        return render(request, 'organization/profile.html', {'text': 'User is Not Logged In'})

def edit_org(request):
    profile = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrganizationProfile(request.POST)
            if form.is_valid():
                contact = form.cleaned_data['contact']
                description = form.cleaned_data['description']
                address = form.cleaned_data['address']

                form_data = Organization(user=request.user, contact=contact, description=description, address=address)
                form_data.save()
        else:
            user = request.user
            try:
                profile = Organization.objects.get(user=user)
            except Organization.DoesNotExist:
                profile = None
            form = OrganizationProfile(instance=profile)

        return render(request, 'organization/edit_org.html', {'form': form, 'profile': profile})
    else:
        return render(request, 'organization/profile.html', {'text': 'User Not Logged In'})


def appointment(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']
                org = Organization.objects.get(pk=id)
                form_data = Appointment(org=org, subject=subject, date=date, time=time)
                form_data.save()
                
        form = AppointmentForm()
        appointments = Appointment.objects.all()
        return render(request, 'organization/appointment.html', {'form': form, 'appointments': appointments})
    else:
        return render(request, 'registration/user_login.html')


def orgs(request):
    orgs = Organization.objects.all()    
    return render(request, 'organization/orgs.html', {'orgs': orgs})