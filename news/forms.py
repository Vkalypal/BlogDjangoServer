from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput


class ArticlesForm(ModelForm):   # класс отвечающий за то, что будет вызвано при обращении к базе
    class Meta:
        model = Articles
        fields = ['title', 'date', 'imageBlog']

        widgets = {   # Словарь для характеристик полей widgets-ключевое слово
            "title": TextInput(attrs={
                'class': 'title-input',
                'placeholder': 'Подпиши свою хуйню'
            }),
            "date": DateTimeInput(attrs={
                'type': 'datetime-local'
            }),
        }
