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
                            'lost','found'
                           ]

    if value.lower() in normal:
        return True
    if is_number(value.lower()):
        return True
    return False




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


    def weight_of_matches(self,tokenList):
        ret=0

        ans=""
        for s in tokenList:
            if not NormalValidator(s):
                ans+=s
            else:
                ans+="_"

        fin=ans.split("_")
        fin=list(filter(None,fin))
        wow=list(set(fin))

        for t in wow:
            if t in self.accountname:
                ret=ret+1

        return ret
