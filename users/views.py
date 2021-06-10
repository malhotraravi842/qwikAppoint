from django.shortcuts import render
from  django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm

# Create your views here.
def users(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(request, 'users/index.html', {'form': form})

def userProfile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm()

    return render(request, 'users/profile.html', {'form': form})
