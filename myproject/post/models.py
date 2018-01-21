from django.db import models




class Post(models.Model):
    status=models.BooleanField()
    posterName=models.CharField(max_length=30)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    location=models.CharField(max_length=100)
    mobileNumber=models.CharField(max_length=35)
    mailid=models.CharField(max_length=50,null=True)
    defintion=models.TextField(blank=True)
    description=models.TextField(blank=True)

    class Meta:
        ordering = ("-date","-time","status")
        db_table = 'dummy_posts'

    def __str__(self):
        return self.posterName

    def get_absolute_url(self):
        return "/posts/%i" %self.id





#class Image(models.Model):

#    caption=models.CharField(max_length=50,null=True,blank=True)
#    imagefile=models.ImageField()
#    postedin=models.ForeignKey(Post,on_delete=models.CASCADE)
