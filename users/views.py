from django.shortcuts import render
from .forms import UserProfileForm


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = UserProfileForm()
        
        return render(request, 'users/profile.html', {'form': form})
    else:
        return render(request, 'users/profile.html', {'text': 'User Not Logged In'})

