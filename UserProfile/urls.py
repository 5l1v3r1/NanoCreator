from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.viewProfile, name='view_profile')
]
