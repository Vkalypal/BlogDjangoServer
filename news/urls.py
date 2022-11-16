from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home') # Вызываем метод index из файла views.py
                                    # Имя добавляется для использования в html файлах вместо прописывания конкретного пути
]