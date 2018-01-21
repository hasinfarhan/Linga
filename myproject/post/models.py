from django.db import models




class Post(models.Model):
    status=models.BooleanField()
    posterName=models.CharField(max_length=30)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    location=models.CharField(max_length=100)
    mobileNumber=models.CharField(max_length=35)
    mailid=models.CharField(max_length=50,null=True)
    defintion=models.TextField(blank=True)
    description=models.TextField(blank=True)

    class Meta:
        ordering = ("-date","-time","status")
        db_table = 'dummy_posts'

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return "/posts/%i" %self.id

    def get_status(self):
        if self.status:
            return "Found"
        else:
            return "Lost"

    def get_mail_status(self):
        if self.mailid:
            return True
        else:
            return False

class PostComment(models.Model):
    commenterName=models.CharField(max_length=30)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    description=models.TextField(blank=False)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        ordering = ("-date","-time")
        db_table = 'dummy_post_comments'

    def __str__(self):
        return self.commenterName




class PostImage(models.Model):

   imagefile=models.ImageField(upload_to="postImages")
   post=models.ForeignKey(Post,on_delete=models.CASCADE)

   class Meta:
       db_table = 'dummy_post_images'

   def __str__(self):
       return self.imagefile
