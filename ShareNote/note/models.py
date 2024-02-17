from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Media(models.Model):
    media_type = models.CharField(max_length=64)
    details = models.CharField(max_length=64)


class Text(models.Model):
    data = models.CharField(max_length=2048)
    style = models.CharField(max_length=64)
    IsBold = models.BooleanField(default=False)
    IsItalic = models.BooleanField(default=False)
    IsUnderline = models.BooleanField(default=False)
    align = models.CharField(max_length=64)
    
class Note(models.Model):
    title = models.CharField(max_length=64)
    medialist = models.ForeignKey(Media,on_delete=models.CASCADE,related_name="MediaOfNote")
    content = models.ForeignKey(Text,on_delete=models.CASCADE,related_name="TextOfNote")
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
    collabs = models.ForeignKey(User,on_delete=models.CASCADE,related_name="collabs")
    label = models.CharField(max_length=64)
    version = models.IntegerField()
    lastModified = models.DateTimeField()

class Template(models.Model):
    title = models.CharField(max_length=64)
    content = models.ForeignKey(Text,on_delete=models.CASCADE,related_name="ContentOfTemp")
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="CreatorOfTemplate")