from django.shortcuts import render
from django.shortcuts import render_to_response
from post.models import Post, Comment, Tag

# Create your views here.

def list_posts(request):
    listofposts = Post.objects.all()
    return render_to_response('paper/index.html', {'listofposts': listofposts})

def filterbytag(request, filter_by_tag):
    print (filter_by_tag)
#    for n in Post.post_tags:
#     print (n)
    fbt = '123'
    return render_to_response('paper/index.html', {'listofposts': fbt})
