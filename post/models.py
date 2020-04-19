from django.db import models


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def NormalValidator(value):
    normal = ['a','an','the','on','up','in','out','do','while','of','up','about','time','over',
                            'to','from','than','that','what','into','bad','was','is','am','with','ago','recent','very','much',
                            'cost','or','else','if','you','i','u','they','he','she','end','doing','cut','person','interest',
                            'away','wait','again','before','less','more','0','1','10','100','another','it',"it's",'are','s','my','your',
                            'lost','found','have','has','had','will','g','gg','ggg','gggg','ggggg','a','aa','aaa'',aaaaa','aaaa','enter',
                            'feel','pass','travel', 'sex', 'orgy',
                           ]

    if value.lower() in normal:
        return True
    if is_number(value.lower()):
        return True
    return False


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

    def get_definition_tags(self):
        ret=""
        for c in self.defintion:
            if (c>='a' and c<='z') or (c>='A' and c<='Z') or (c>='0' and c<='9'):
                ret+=c
            else:
                ret+='_'
        tags=ret.split("_")

        ans=""
        for s in tags:
            if not NormalValidator(s):
                ans+=s.lower()
            ans+="_"

        fin=ans.split("_")
        fin=list(filter(None,fin))

        wow=list(set(fin))
        return wow

    def get_description_tags(self):
        ret=""
        for c in self.description:
            if (c>='a' and c<='z') or (c>='A' and c<='Z') or (c>='0' and c<='9'):
                ret+=c
            else:
                ret+='_'
        tags=ret.split("_")

        ans=""
        for s in tags:
            if not NormalValidator(s):
                ans+=s.lower()
            ans+="_"

        fin=ans.split("_")
        fin=list(filter(None,fin))

        wow=list(set(fin))
        return wow
    def get_location_tags(self):
        ret=""
        for c in self.location:
            if (c>='a' and c<='z') or (c>='A' and c<='Z') or (c>='0' and c<='9'):
                ret+=c
            else:
                ret+='_'
        tags=ret.split("_")

        ans=""
        for s in tags:
            if not NormalValidator(s):
                ans+=s.lower()
            ans+="_"

        fin=ans.split("_")
        fin=list(filter(None,fin))

        wow=list(set(fin))
        return wow


    def weight_of_matches(self,tokenList):
        ret=0

        ans=""
        for s in tokenList:
            if not NormalValidator(s):
                ans+=s.lower()
            else:
                ans+="_"

        fin=ans.split("_")
        fin=list(filter(None,fin))
        wow=list(set(fin))

        for t in wow:
            if t in self.get_definition_tags() or t in self.get_description_tags() or t in self.get_location_tags() or self.defintion.lower() in t or self.description.lower() in t or self.location.lower() in t:
                ret=ret+1

        return ret







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
