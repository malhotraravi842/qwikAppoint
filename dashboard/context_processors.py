from .models import Profile
import  json

def message_processor(request):
    org_data = json.dumps(list(Profile.objects.values()))
    return  {
        'org_data': org_data,
    }