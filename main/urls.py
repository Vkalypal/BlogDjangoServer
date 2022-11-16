from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # Вызываем метод index из файла views.py
    path('contacts', views.contacts, name='contacts')    # Имя добавляется для использования в html файлах вместо прописывания конкретного пути
]