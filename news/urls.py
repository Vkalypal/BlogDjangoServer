from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'), # Вызываем метод news_home из файла views.py
    path('create', views.create, name='create')  # Имя добавляется для использования в html файлах вместо прописывания конкретного пути
]