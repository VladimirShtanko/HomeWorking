from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-name'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['bad_words'] = ['редиска','редиску','редиски']
        context['next_sale'] = None
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'