"""NanoSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from core import views as core_views
from Authentication import views as auth_views2
urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    ## url(r'^accounts/login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/login/', auth_views2.login_view, name='login'),
    url(r'^accounts/regis/', auth_views2.regis_view, name='regis'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    url(r'^accounts/profile/$', core_views.home, name='profile'),
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
