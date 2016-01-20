from django.contrib import admin
from post.models import Tag, Post, Comment

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

