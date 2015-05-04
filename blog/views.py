from blog.models import BlogPost
from django.shortcuts import render


def archive(request):
    """
    Return list of all posts
    """
    posts = BlogPost.objects.all()
    context = {'posts': posts}

    return render(request, 'archive.jinja', context)
