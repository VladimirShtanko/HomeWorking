
from django_filters.views import FilterView
import django_filters
from django import forms
from .models import Post



class PostFilter(django_filters.FilterSet):
    # Поиск по названию (name)
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',  # нечувствительно к регистру
        label='Название'
    )
    # Поиск по автору
    author__username = django_filters.CharFilter(
        field_name='author_name',
        lookup_expr='icontains',
        label='Автор'
    )
    # По дате позже указанной
    date = django_filters.DateFilter(
        field_name='datepublic',
        lookup_expr='gte',  # больше или равно
        widget=forms.DateInput(attrs={'type': 'datepublic'}),
        label='Дата с'
    )

    class Meta:
        model = Post
        fields = ['name', 'author__username', 'datepublic']


class NewsSearchList(FilterView):
    model = Post
    template_name = 'search.html'
    filterset_class = PostFilter
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(type='news').order_by('-datepublic')