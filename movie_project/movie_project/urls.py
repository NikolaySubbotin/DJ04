from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('films/', include('films.urls')),  # Все маршруты из приложения films
    path('', lambda request: HttpResponseRedirect('/films/')),  # Перенаправление на фильмы с главной
]
