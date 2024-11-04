from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import AllowAny
from .serialezar import createMovieSerializer, MovieSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class create(APIView):
    def post(self, request):
        serializer = createMovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if Movie.objects.filter(name_movie=serializer.validated_data['name_movie']).exists():

            return Response("the movie name it is repeated", status=status.HTTP_400_BAD_REQUEST)
        Movie.objects.create(**serializer.validated_data)
        return Response('the movie create successful ', status= status.HTTP_201_CREATED)
        
   

class read(APIView):
    def get(self, request):
        name_movie = request.query_params.get('name_movie', None)
        if name_movie:
            # Filtrar por nombre si se proporciona el parámetro
            movies = Movie.objects.filter(name_movie__iexact=name_movie)
        else:
            # Obtener todas las películas si no se especifica el nombre
            movies = Movie.objects.all()
        
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   

class update(APIView):
    def put(self, request, name_movie):
        # Busca la película por su nombre
        movie = get_object_or_404(Movie, name_movie=name_movie)
        
        # Crea un serializer con los datos existentes y actualiza con los nuevos datos
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        
        # Valida y guarda los datos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   