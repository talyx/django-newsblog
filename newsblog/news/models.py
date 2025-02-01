from django.db import models


# Create your models here.

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    ful_text = models.TextField('Новость')
    date = models.DateTimeField('Дата публикации')

    def get_absolute_url(self):
        return f'/{self.id}'

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'