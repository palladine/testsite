from django.forms import ModelForm
from post.models import Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CommentForm(ModelForm):
    class Meta():
         model = Comment
         fields = ['comment_author', 'comment_text']
         widgets = {
          'comment_text': SummernoteWidget(),
         }
