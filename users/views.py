from django.shortcuts import render
from .forms import ProfileForm, UserForm

# Create your views here.
def users(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    
    return render(request=request, template_name="users/user.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })