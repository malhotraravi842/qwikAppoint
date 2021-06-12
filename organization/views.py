from django.shortcuts import render
from .forms import OrganizationProfile


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

