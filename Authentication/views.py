from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # submit login button was pressed
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'core/home.html')
        else:
            # return invalid login
            messages.error(request, 'username or password not correct')
    return render(request, 'Login_v4/index.html')

def regis_view(request):
    return render(request, 'Regis_v4/index.html')
