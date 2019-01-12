from django.shortcuts import render
from .models  import UserProfile

# Create your views here.
def viewProfile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except Exception as e:
        print(e)
        ## should return 'setup_profile'. ## first time setup. (new account)
        return render(request, "UserProfile/profile_not_found.html")
    context = {'user_profile' : user_profile}
    return render(request, 'UserProfile/profile.html', context)
