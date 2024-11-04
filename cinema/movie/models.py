from django.db import models

# Create your models here.
class Movie(models.Model):
    name_movie = models.CharField(max_length=100, null=False)
    classification_movie = models.CharField(max_length=100, null=False)
    gender_movie = models.CharField(max_length=100, null=False)
    release_date = models.DateField(null=False)  # `max_length` no es necesario para DateField
 
    
    
