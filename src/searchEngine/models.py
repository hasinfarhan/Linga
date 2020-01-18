from django.db import models

class SearchKey(models.Model):
    keyword=models.CharField(max_length=150)
    #post=models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        #ordering = ("-date","-time")
        db_table = 'dummy_keywords'

        def __str__(self):
            return self.keyword
