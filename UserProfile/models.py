from django.db import models
from django.contrib.auth.models import User
import NanoSite.settings as settings
import datetime

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True)
    gender = models.CharField(max_length=8, default='404')
    birthday = models.DateField(
        null=True,
        default=datetime.date.today
        )
    phone = models.IntegerField(default=-1)
    subject = models.CharField(max_length=32, default='Other')
    def __str__(self):
        return 'Profile - ' + self.user.username
