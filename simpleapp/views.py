from datetime import datetime
from django.urls import reverse_lazy
from simpleapp.forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from .models import Post
from .filters import NewsFilter





class NewsSearchView(ListView):
    model = Post
    filterset_class = NewsFilter
    ordering = 'name'
    template_name = 'search.html'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



class PostsList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['bad_words'] = ['редиска','редиску','редиски']
        context['next_sale'] = None
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class NewsPostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = Post.NEWS  # Установим тип на "новость"
        post.save()
        return super().form_valid(form)

class NewsPostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_post_edit.html'

class NewsPostDelete(DeleteView):
    model = Post
    template_name = 'news_post_delete.html'
    success_url = reverse_lazy('post_list')

class ArticlePostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = Post.ARTICLE  # Установим тип на "новость"
        post.save()
        return super().form_valid(form)

class ArticlePostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_post_edit.html'

class ArticlePostDelete(DeleteView):
    model = Post
    template_name = 'article_post_delete.html'
    success_url = reverse_lazy('post_list')


