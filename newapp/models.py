from django.db import models

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=264)
    emailid = models.EmailField(max_length=264)
    subject = models.CharField(max_length=200,default="null")
    messages = models.CharField(max_length=264,default="null")

   
    class Meta:
        db_table = "signup"

class hm(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)
    contactt = models.IntegerField()
    destination= models.CharField(max_length=264)

   
    class Meta:
        db_table = "hm"

