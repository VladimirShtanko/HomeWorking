from _datetime import timezone
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator


# Товар для нашей витрины
class Post(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    datepublic = models.DateTimeField(default=timezone.now)
    description = models.TextField()


    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='allposts', # все продукты в категории будут доступны через поле products
    )


    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
