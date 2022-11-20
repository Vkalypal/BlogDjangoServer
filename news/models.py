from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    date = models.DateTimeField('Дата публикации')
    imageBlog = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):    # Метод отображения содержимого базы
        return f'Новость: {self.title}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
