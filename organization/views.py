from django.shortcuts import render

# Create your views here.
def organization(request):
    return render(request, 'organization/index.html')