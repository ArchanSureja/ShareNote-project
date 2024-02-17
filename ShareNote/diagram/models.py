from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Shape(models.Model):
    ShapeType = models.CharField(max_length=64)
    cord1 = models.DecimalField(max_digit=10, decimal_places=5)
    cord2 = models.DecimalField(max_digit=10,decimal_places=5)
    Text = models.CharField()

class Diagram(models.Model):
    title = models.CharField(max_length=64)
    content = models.ForeignKey(Shape,on_delete=models.CASCADE,related_name="ShapesOfDiagram")
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
    collabs = models.ForeignKey(User,on_delete=models.CASCADE,related_name="collabs")
    label = models.CharField(max_length=64)
    version = models.IntegerField()
    lastModified = models.DateTimeField()


    # we store shape as json format then at rendering time we use draw.io js library to render the diagram from json format 