from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'Login_v4/index.html')

def regis_view(request):
    return render(request, 'Regis_v4/index.html')
