from django.db import models


from django.db import models



class Post(models.Model):

    title=models.CharField(max_length=50,unique=True)
    accountName=models.CharField(max_length=30)
    dateTime=models.DateTimeField(auto_now=True)
    primaryLocation=models.CharField(max_length=100)
    secondaryLocation=models.CharField(max_length=100,null=True)
    contactNumbers=models.CharField(max_length=50)
    mailid=models.CharField(max_length=50,null=True)
    externalLink=models.URLField(null=True)
    dynamic=models.BooleanField()
    description=models.TextField(blank=True)



class DummyPost(models.Model):

    status=models.BooleanField()
    posterName=models.CharField(max_length=30)
    dateTime=models.DateTimeField(auto_now=True)
    location=models.CharField(max_length=100)
    contactNumber=models.CharField(max_length=35)
    mailid=models.CharField(max_length=50,null=True)
    defintion=models.TextField(blank=True)
    description=models.TextField(blank=True)



class Image(models.Model):

    caption=models.CharField(max_length=50,null=True,blank=True)
    imagefile=models.ImageField()
    postedin=models.ForeignKey(Post,on_delete=models.CASCADE)
