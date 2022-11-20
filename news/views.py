from django.shortcuts import render, redirect
from .models import Articles  # Импортируем из файла models класс Articles
from .forms import ArticlesForm # Импортируем из файла forms класс ArticlesForm


# Create your views here.


def news_home(request):
    news = Articles.objects.order_by('-date') # Получаем все объекты из класса. Сортируем по дате
    return render(request, 'news/news_home.html', {'news': news}) # Передаем по ключу news обьект news


def create(request):
    error = ''
    if request.method == 'POST': # Если метод передачи данных POST, то есть из формы то
        form = ArticlesForm(request.POST, request.FILES) # записываем данные которые пришли из формы в объект form
        # request.FILES для передачи картинок
        if form.is_valid():  # Если все данные полей корректно заполнены
            form.save()      # то сохраняем данные в базу
            return redirect('news_home') # переадресация на страницу home
        else:
            error = 'Форма заполнена неверно'
    form = ArticlesForm()  # Создаем объект на основе класса ArticlesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)