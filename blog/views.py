from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from .models import BlogPost, Category
from .forms import CommentForm
from django.urls import reverse_lazy


# Create your views here.
def Home(request):
    template_name = 'home.html'
    posts = BlogPost.objects.filter(status='published').order_by('-created')
    context = {'posts': posts}
    return render(request, template_name, context)

def Blog(request):
    queryset = BlogPost.objects.filter(status = 'published').order_by('-created')
    per_page = 3
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    # <QueryDict: {'page':[2]} -request.GET

    template_name = 'Blog/blog.html'
    context = {'posts': posts}
    return render(request, template_name, context)

def single_post(request, slug):
    post = get_object_or_404(BlogPost, slug= slug)
    template_name = 'Blog/single.html'
    context = {'post': post}
    return render(request, template_name, context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = BlogPost.objects.filter(category=category, status='published').order_by('-created')
    template_name = 'blog.html'
    context = {'posts': posts}
    return render(request, template_name, context)

