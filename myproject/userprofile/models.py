from django.db import models
from django.contrib.auth.models import User










class UserProfile(models.Model):

    #user=models.OneToOneField(User)

    primaryAddress=models.CharField(max_length=100,null=True, blank=True)
    #contactNumber=models.CharField(max_length=35,null=True, blank=True)

    #secondaryAddress=models.CharField(max_length=100,null=True, blank=True)
