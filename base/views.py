from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post, Topic
import markdown

# Create your views here.

# rooms = [
#     {"id": 1, "name": "Let's learn python"},
#     {"id": 2, "name": "Developer"},
#     {"id": 3, "name": "Suwi stuff"},
    
# ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    post = Post.objects.filter(topic__name__icontains=q)
    topics = Topic.objects.all()

    context = {"post":post,
               "topics": topics}
    return render(request, 'base/home new.html', context)

def latestPosts(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    post = Post.objects.filter(topic__name__icontains=q)
    topics = Topic.objects.all()

    context = {"post":post,
               "topics": topics}
    return render(request, 'base/latest posts.html', context)

def about(request):
    return render(request, 'base/about.html')

def post(request, pk):
    post = Post.objects.get(url=pk)
    body1 = markdown.markdown(post.body1)
    body2 = markdown.markdown(post.body2)
    body3 = markdown.markdown(post.body3)
    description = markdown.markdown(post.description)
    context = {'post': post,
               'body1': body1,
               'body2': body2,
               'body3': body3,
               'description': description}
    return render(request, 'base/post.html', context)

def test(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    post = Post.objects.filter(topic__name__icontains=q)
    topics = Topic.objects.all()

    context = {"post":post,
               "topics": topics}
    return render(request, 'base/home old.html', context)


 


