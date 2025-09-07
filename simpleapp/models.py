from _datetime import timezone

from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator


# Товар для нашей витрины
class Post(models.Model):

    NEWS = 'news'
    ARTICLE = 'article'
    TYPE_CHOICES = [
        (NEWS, 'News'),
        (ARTICLE, 'Article'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=NEWS)

    name = models.CharField(
        max_length=50,
        unique=True,
    )
    datepublic = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author_name = models.CharField(max_length=100 , default= 'Автор')


    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='allposts',
    )




    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])



class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


from django.db import models


