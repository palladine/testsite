from django.db import models

# Create your models here.
class Tag(models.Model):
    class Meta():
        db_table = 'tags'
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'
    tag = models.CharField(max_length = 15, verbose_name='Тег', unique=True)

    def __str__(self):
        return self.tag

class Post(models.Model):
    class Meta():
        db_table = 'posts'
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ['-post_date']
    post_title = models.CharField(max_length = 200, verbose_name='Название поста', unique=True)
    post_text = models.TextField(verbose_name='Текст поста')
    post_date = models.DateTimeField(verbose_name='Дата и время написания поста', auto_now_add=True)
    post_author = models.CharField(max_length = 25, verbose_name='Автор поста')
    post_tags = models.ManyToManyField(Tag, verbose_name='Теги')

    def __str__(self):
        return '%s [Автор: %s]' % (self.post_title, self.post_author)

class Comment(models.Model):
    class Meta():
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-comment_date']
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_post = models.ForeignKey(Post, verbose_name='Комментарии')
    comment_date = models.DateTimeField(verbose_name='Дата и время написания комментария', auto_now_add=True)
    comment_author = models.CharField(max_length = 25, verbose_name='Автор комментария')
 
    def __str__(self):
        return '%s [Автор: %s]' % (self.comment_date, self.comment_author) 




