from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
 
def index (request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'blogapp/index.html', context)

def create (request):
    return render(request, 'blogapp/create.html')

def createpost (request):
    post = Post(title=request.POST['title'], content=request.POST['content'], imageurl=request.POST['imageurl'])
    post.save()
    return HttpResponseRedirect(reverse('index'))

def detailpost (request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blogapp/detail.html', context)

def editpost (request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blogapp/edit.html', context)

def savepost (request, post_id):
    post = Post.objects.get(pk=post_id)
    post.title=request.POST['title']
    post.content=request.POST['content']
    post.imageurl=request.POST['imageurl']
    post.save()
    context = {
        'post': post
    }
    return HttpResponseRedirect('/blog/' + str(post.id))
    # return HttpResponseRedirect(reverse('detailpost'))