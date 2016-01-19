from django.shortcuts import render
from django.shortcuts import render_to_response
from post.models import Post, Comment, Tag

# Create your views here.

def list_posts(request):
    listofposts = Post.objects.all()
    return render_to_response('index.html', {'listofposts': listofposts[0]})

