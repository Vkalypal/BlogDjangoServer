from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):   # класс отвечающий за то, что будет вызвано при обращении к базе
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {   # Словарь для характеристик полей widgets-ключевое слово
            "title": TextInput(attrs={
                'class': 'title-input',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'title-input',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'type': 'datetime-local'
            }),
            "full_text": Textarea(attrs={
                'class': 'title-input',
                'placeholder': 'Текст статьи'
            })
        }
