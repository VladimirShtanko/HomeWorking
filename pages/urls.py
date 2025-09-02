from django.urls import path
from django.contrib.flatpages.views import flatpage

urlpatterns = [
    path('about/', flatpage, {'slug': 'about/'}, name='about'),
    path('adminonly/', flatpage, {'slug': 'adminonly/'}, name='adminonly'),
]