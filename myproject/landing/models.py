from django.db import models


class Profile(models.Model):
    mailid=models.CharField(max_length=75)
    password1=models.CharField(max_length=30)
    accountname=models.CharField(max_length=40)
    primaryaddress=models.CharField(max_length=100, blank=True)
    contactnumber=models.CharField(max_length=35, blank=True)



    class Meta:
        ordering = ("accountname","mailid")
        db_table = 'profile_Data'

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return "/posts/%i" %self.id


    def get_mail_status(self):
        if self.mailid:
            return True
        else:
            return False
