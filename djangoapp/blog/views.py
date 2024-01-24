from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post,Page,Category
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404

POST_PER_PAGE = 15

def index(request):
    posts = Post.objects.get_published()
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title':'Home',
        }
    )

def created_by(request, author_pk):
    user = User.objects.filter(pk=author_pk).first()
    if user is None:
        raise Http404()
    
    posts = Post.objects.get_published().filter(created_by__pk=author_pk)
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': f'{user.first_name} {user.last_name} posts'\
                  if user.first_name else f'{user.username} posts'
        }
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)
    
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    page_title = page_obj[0].category.title

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title
        }
    )

def tag(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)
    
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    page_title = page_obj[0].tags.filter(slug=slug).first().name

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title':page_title
        }
    )

def search(request):
    search_value = request.GET.get('search',None).strip()
    posts = (Post.objects.get_published()
             .filter(
                Q(title__icontains=search_value) |
                Q(excerpt__icontains=search_value) |
                Q(content__icontains=search_value)
             ))
    
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'search_value':search_value,
            'page_title':f'"{search_value}"'
        }
    )


def page(request,slug):
    page_obj = Page.objects.filter(is_published=True).filter(slug=slug).first()

    if page_obj is None:
        raise Http404()
        

    return render(
        request,
        'blog/pages/page.html',
        {
            'page':page_obj,
            'page_title':page_obj.title
        }
    )


def post(request,slug):
    post_obj = Post.objects.get_published().filter(slug=slug).first()

    if post_obj is None:
        raise Http404()

    return render(
        request,
        'blog/pages/post.html',
        {
            'post':post_obj,
            'page_title':post_obj.title
        }
    )