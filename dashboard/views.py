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

# Create your views here.

def homepage(request):
    return render(request, 'dashboard/index.html')

def signup(request):
    if request.method == 'POST':
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


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                type = form.cleaned_data['type']
                contact = form.cleaned_data['contact']
                bio = form.cleaned_data['bio']
                address = form.cleaned_data['address']
                pincode = form.cleaned_data['pincode']

                form_data = Profile(user=request.user, type=type, contact=contact, bio=bio, address=address, pincode=pincode)
                form_data.save()
        else:
            user = request.user
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                profile = None
            form = ProfileForm(instance=profile)
        return render(request, 'dashboard/profile.html', {'form': form, 'profile': 'profile'})
    else:
        return render(request, 'dashboard/profile.html', {'text': 'User is Not Logged In'})