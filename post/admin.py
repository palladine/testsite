from django.contrib import admin
from post.models import Tag, Post, Comment

# Register your models here.

#class TagAdmin(admin.ModelAdmin):
#    list_display = ('tag',)

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('comment_date',)
    list_filter = ['comment_date', 'comment_author']

class CommentsInLine(admin.StackedInline):
    model = Comment
    extra = 2

class PostAdmin(admin.ModelAdmin):
    list_filter = ('post_date', 'post_author')
    inlines = [CommentsInLine,]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)

