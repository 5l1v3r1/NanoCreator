from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login_view, name='login'),
    url(r'^regis/', views.regis_view, name='regis'),
]
