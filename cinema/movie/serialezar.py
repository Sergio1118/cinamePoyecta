from rest_framework import serializers
from .models import Movie

class createMovieSerializer(serializers.ModelSerializer):
    name_movie=serializers.CharField()
    classification_movie=serializers.CharField()
    gender_movie=serializers.CharField()
    release_date=serializers.DateField()
    class Meta:
        model = Movie  # Especifica el modelo a utilizar
        fields = '__all__'
   
   
   
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
   