from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .models import UserProfile

def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                about = form.cleaned_data['about']
                contact = form.cleaned_data['contact']
                location = form.cleaned_data['location']
                birth_date = form.cleaned_data['birth_date']

                form_data = UserProfile(user=request.user, about=about, contact=contact, location=location, birth_date=birth_date)
                form_data.save()
        else:
            user = request.user
            try:
                profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                profile = None
            form = UserProfileForm(instance=profile)

        return render(request, 'users/edit_profile.html', {'form': form})
    else:
        return render(request, 'users/profile.html', {'text': 'User Not Logged In'})

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html', {'user': request.user})
    else:
        return render(request, 'users/profile.html', {'text': 'User Not Logged In'})

