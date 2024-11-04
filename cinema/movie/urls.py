from django.urls import path
from . import views

# para un espacion se ultilice el %20 en las urls

urlpatterns = [
    path('create/',views.create.as_view(),name='create'),
    path('read/', views.read.as_view(),name='read'),
    path('update/<str:name_movie>/',views.update.as_view(),name='update'),
]