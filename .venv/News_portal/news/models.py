from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models



class Author (models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    rating = models.IntegerField (default= 0)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        #Post reiting
        post_rating = sum(post.rating * 3 for post in self.post_set.all())

        #Comment avtor
        comment_avtor_reiting = sum(comment.rating for comment in self.user.comment_set.all())

        #Comment avtor in post
        comment_ratings_on_author_posts = sum(comment.rating for post in self.post_set.all() for comment in post.comment_set.all())

        self.rating = post_rating + comment_avtor_reiting + comment_ratings_on_author_posts
        self.save()

class Category(models.Model):
    name = models.CharField(max_length= 255 , unique= True)

    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY = (
        ('article', 'Статьи'),
        ('news', 'Новости')
)

    avtor = models.ForeignKey (Author , on_delete=models.CASCADE)
    post_vibor = models.CharField(max_length= 10 , choices=CATEGORY)
    data_and_time_create = models.DateTimeField(default= timezone.now)
    category = models.ManyToManyField(Category , through= 'PostCategory')
    title = models.CharField (max_length= 255 )
    text = models.TextField()
    rating = models.IntegerField(default= 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.text) > 124:
            return self.text[:124] + '...'
        return self.text

    def __str__(self):
        return self.title

class PostCategory (models.Model):
    post = models.ForeignKey(Post , on_delete= models.CASCADE)
    category = models.ForeignKey(Category ,  on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.post.title} - {self.category.name}"


class Comment (models.Model):
    post = models.ForeignKey(Post ,  on_delete= models.CASCADE)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    text = models.TextField()
    data_and_time_create = models.DateTimeField(default= timezone.now)
    rating = models.IntegerField(default= 0)


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'Комментарии от {self.user.username} к {self.post.title}'