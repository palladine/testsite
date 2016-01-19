from django.contrib import admin
from post.models import Tag, Post, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)

