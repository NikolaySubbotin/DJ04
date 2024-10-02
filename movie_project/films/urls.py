from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_film, name='add_film'),  # Маршрут для добавления фильма
    path('', views.film_list, name='film_list'),  # Маршрут для списка фильмов
]
