from django.shortcuts import render
from django.shortcuts import render_to_response
from post.models import Post, Comment, Tag

# Create your views here.

def list_posts(request):
    listofposts = Post.objects.all()
    return render_to_response('paper/index.html', {'listofposts': listofposts})

def postbyid(request, post_id):
    fieldstopost = Post.objects.get(id=post_id)
    return render_to_response('paper/post.html', {'postfull': fieldstopost})

def postsbytag(request, tag_name):
    tag = Tag.objects.select_related().get(tag=tag_name)
    postsoftag = tag.post_set.all()
    return render_to_response('paper/tags.html', {'selecttag': tag, 'postsoftag': postsoftag})
