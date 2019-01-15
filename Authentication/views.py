from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        first_name  = request.POST['first_name']
        last_name   = request.POST['last_name']
        birthday    = request.POST['birthday']
        gender      = request.POST['gender']
        email       = request.POST['email']
        phone       = request.POST['phone']
        subject     = request.POST['subject']
        username    = first_name + " " + last_name
        password    = 'password'
        new_user    = User.objects.create_user(
            username=username,
            email=email,
            password=password
            )
        new_user.first_name = first_name
        new_user.last_name  = last_name
        new_user.save()
        login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
            )
        return redirect('home')
    return render(request, 'Regis_v4/index.html')
