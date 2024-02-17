from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Shape(models.Model):
    ShapeType = models.CharField(max_length=64)
    cord1 = models.FloatField()
    cord2 = models.FloatField()
    Text = models.CharField(max_length=64)

class Diagram(models.Model):
    title = models.CharField(max_length=64)
    content = models.ForeignKey(Shape,on_delete=models.CASCADE,related_name="ShapesOfDiagram")
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="CreatorOfDiagram")
    collabs = models.ForeignKey(User,on_delete=models.CASCADE,related_name="collabsOfDiagram")
    label = models.CharField(max_length=64)
    version = models.IntegerField()
    lastModified = models.DateTimeField()


    # we store shape as json format then at rendering time we use draw.io js library to render the diagram from json format 