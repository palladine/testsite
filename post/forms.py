from django.forms import ModelForm
from post.models import Comment

class CommentForm(ModelForm):
    class Meta():
         model = Comment
         fields = ['comment_author', 'comment_text']
        
