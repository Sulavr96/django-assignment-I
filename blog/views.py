from django.shortcuts import render, get_list_or_404
from blog.models import Author, Blog
# Create your views here.


def home(request):
    return render(request, 'home.html')

def author(request):
    authors = Author.objects.all()
    context = { 'authors': authors }
    return render(request, 'author.html', context=context)


def blog(request, author_id):
    author_blogs = get_list_or_404(Blog, author_id=author_id)
    author_name = author_blogs[0].author
    context = {'blogs': author_blogs,
               'author_name': author_name
               }
    return render(request, 'blogs.html', context=context)
