from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio),
    path(
        "imagen-aleatoria/",
        views.imagen_aleatoria,
        name="imagen_aleatoria"
    ),

]