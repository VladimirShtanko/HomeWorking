
from django.urls import path
from .views import  PostsList , NewsSearchView ,  PostDetail , NewsPostCreate , NewsPostUpdate , NewsPostDelete , ArticlePostCreate , ArticlePostDelete , ArticlePostUpdate


urlpatterns = [
   path('', PostsList.as_view() , name='post_list'),
   path('<int:pk>', PostDetail.as_view() , name='post_detail'),
   path('news/create/', NewsPostCreate.as_view(), name='news_post_create'),
   path('news/<int:pk>/edit/', NewsPostUpdate.as_view(), name='news_post_update'),
   path('news/<int:pk>/delete/', NewsPostDelete.as_view(), name='news_post_delete'),
   path('article/create/', ArticlePostCreate.as_view(), name='article_post_create'),
   path('article/<int:pk>/edit/', ArticlePostUpdate.as_view(), name='article_post_update'),
   path('article/<int:pk>/delete/', ArticlePostDelete.as_view(), name='article_post_delete'),
   path('search/', NewsSearchView.as_view(), name='search_post'),
]