from django.db import models

# Create your models here.

class Tag(models.Model):
    class Meta():
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'
    tag = models.CharField(max_length = 15, verbose_name='Тег')

class Post(models.Model):
    class Meta():
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
    post_title = models.CharField(max_length = 200, verbose_name='Название поста', unique=True)
    post_text = models.TextField(verbose_name='Текст поста')
    post_date = models.DateTimeField(verbose_name='Дата и время написания поста', auto_now_add=True)
    post_author = models.CharField(max_length = 25, verbose_name='Автор поста')
    post_tags = models.ManyToManyField(Tag, verbose_name='Теги поста')

class Comment(models.Model):
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_post = models.ForeignKey(Post)
    comment_date = models.DateTimeField(verbose_name='Дата и время написания комментария', auto_now_add=True)
    comment_author = models.CharField(max_length = 25, verbose_name='Автор комментария')



