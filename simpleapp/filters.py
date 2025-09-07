from cProfile import label
from django_filters import FilterSet
from .models import Post
import django_filters



class NewsFilter(FilterSet):
    name = django_filters.CharFilter()
    author_name = django_filters.CharFilter()
    datepublic = django_filters.DateFromToRangeFilter(field_name='datepublic', label='Дата публикации (от - до)')

    class Meta:
        model = Post
        fields = {
            'name': [],
            'author_name': [],
            'datepublic': ['exact']
        }