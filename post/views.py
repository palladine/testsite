from django.shortcuts import render
from django.shortcuts import render_to_response
from post.models import Post, Comment, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def list_posts(request):
    getlistofposts = Post.objects.all()
    paginator = Paginator(getlistofposts, 1)
    page = request.GET.get('page')
    try:
        listofposts = paginator.page(page)
    except PageNotAnInteger:
        listofposts = paginator.page(1)
    except EmptyPage:
        listofposts = paginator.page(paginator.num_pages)
    return render_to_response('paper/index.html', {'listofposts': listofposts})



def postbyid(request, post_id):
    fieldstopost = Post.objects.get(id=post_id)
    return render_to_response('paper/post.html', {'postfull': fieldstopost})



def postsbytag(request, tag_name):
    tag = Tag.objects.select_related().get(tag=tag_name)
    getposts = tag.post_set.all()
    paginator = Paginator(getposts, 1)
    page = request.GET.get('page')
    try:
        postsoftag = paginator.page(page)
    except PageNotAnInteger:
        postsoftag = paginator.page(1)
    except EmptyPage:
        postsoftag = paginator.page(paginator.num_pages)
    return render_to_response('paper/tags.html', 
            {'getposts': getposts, 'selecttag': tag, 'postsoftag': postsoftag})




