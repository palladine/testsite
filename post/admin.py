from django.contrib import admin
from post.models import Tag, Post, Comment

# Register your models here.

#class TagAdmin(admin.ModelAdmin):
#    list_display = ('tag',)

class CommentsInLine(admin.StackedInline):
    model = Comment
    extra = 2

class PostAdmin(admin.ModelAdmin):
    list_filter = ('post_date',)
    inlines = [CommentsInLine,]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

