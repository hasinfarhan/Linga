from django.db import models





#class Post(models.Model):

#    title=models.CharField(max_length=50,unique=True)
#    accountName=models.CharField(max_length=30)
#    dateTime=models.DateTimeField(auto_now=True)
#    primaryLocation=models.CharField(max_length=100)
#    secondaryLocation=models.CharField(max_length=100,null=True)
#    mobileNumbers=models.CharField(max_length=50)
#    mailid=models.CharField(max_length=50,null=True)
#    description=models.TextField(blank=True)



class DummyPost(models.Model):
    postid=models.IntegerField(unique=True)
    status=models.BooleanField()
    posterName=models.CharField(max_length=30)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    location=models.CharField(max_length=100)
    mobileNumber=models.CharField(max_length=35)
    mailid=models.CharField(max_length=50)
    defintion=models.TextField(blank=True)
    description=models.TextField(blank=True)

    class Meta:
        ordering = ("-date","-time","status")
        db_table = 'dummy_posts'

    def __str__(self):
        return self.posterName

    def get_absolute_url(self):
        return "/dummy1/%i/" %self.postid





#class Image(models.Model):

#    caption=models.CharField(max_length=50,null=True,blank=True)
#    imagefile=models.ImageField()
#    postedin=models.ForeignKey(Post,on_delete=models.CASCADE)
