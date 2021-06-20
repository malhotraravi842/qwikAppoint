from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import RegistrationForm, ProfileForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.auth.models import User
from .models import Profile
from organization.models import Appointment

from django.views.generic import ListView
import json
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None
        return render(request, 'dashboard/dashboard.html', {'profile': profile})
    else:
        return render(request, 'dashboard/index.html')

def signup(request, *args):
    if request.method == 'POST':
        if args:
            print(args[0])

        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Account.'
            message = render_to_string('registration/mail.html', {
                'user': User,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def edit_profile(request, id):
    if request.method == 'POST':
        profile = Profile.objects.get(pk=id)
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
    else:
        profile = Profile.objects.get(pk=id)
        form = ProfileForm(instance=profile)

    return render(request, 'dashboard/edit_profile.html', {'form': form})


# def user_profile(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = ProfileForm(request.POST)
#             if form.is_valid():
#                 type = form.cleaned_data['type']
#                 contact = form.cleaned_data['contact']
#                 bio = form.cleaned_data['bio']
#                 address = form.cleaned_data['address']
#                 pincode = form.cleaned_data['pincode']

#                 form_data = Profile(user=request.user, type=type, contact=contact, bio=bio, address=address, pincode=pincode)
#                 form_data.save()
#         else:
#             user = request.user
#             try:
#                 profile = Profile.objects.get(user=user)
#             except Profile.DoesNotExist:
#                 profile = None
#             form = ProfileForm(instance=profile)
#         return render(request, 'dashboard/profile.html', {'form': form, 'profile': 'profile'})
#     else:
#         return render(request, 'dashboard/profile.html', {'text': 'User is Not Logged In'})



def create_profile(request, type):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                full_name = form.cleaned_data['full_name']
                contact = form.cleaned_data['contact']
                bio = form.cleaned_data['bio']
                address = form.cleaned_data['address']
                pincode = form.cleaned_data['pincode']
                form_data = Profile(user=request.user, full_name=full_name, type=type , contact=contact, bio=bio, address=address, pincode=pincode)
                form_data.save()
            return HttpResponseRedirect('/profile/' + request.user.username + '/')

        form = ProfileForm()

        return render(request, 'dashboard/profile.html', {'form': form})


def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'dashboard/profile.html', {'profile': profile})


# class SearchView(ListView):
#     model = Profile
#     template_name = 'dashboard/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs_json"] = json.dumps(list(Profile.objects.values()))

#         return context