from django.shortcuts import render
# Create your views here.


def index(request):    # Для хранения html и css страниц создаём папку templates, а внутри еще папку с названием приложения
    data = {             # Словарь, по которому передаем значения в шаблоны html
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data) # внутри папки создаем файл html. Этот метод вызывает файл html


def contacts(request):
    return render(request, 'main/contacts.html')