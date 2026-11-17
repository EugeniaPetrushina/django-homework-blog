
from django.db import models


class Review(models.Model):
    full_name = models.CharField('ФИО', max_length=150)
    email = models.EmailField('Email')
    text = models.TextField('Текст отзыва')
    checked = models.BooleanField('Проверено', default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
