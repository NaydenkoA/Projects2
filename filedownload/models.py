from django.db import models

class Libr(models.Model):
    title = models.CharField('Назва книги', max_length=50)
    author = models.CharField('Автори', max_length=50)
    source = models.CharField('Завантажив', max_length=50, default="Адмін")
    file = models.FileField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'