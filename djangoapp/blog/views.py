from django.core.paginator import Paginator
from django.shortcuts import render
from blog.models import Post

POST_PER_PAGE = 15

def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-pk')
    paginator = Paginator(posts, POST_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def page(request):

    return render(
        request,
        'blog/pages/page.html',
        {
            # 'page_obj': page_obj,
        }
    )


def post(request):

    return render(
        request,
        'blog/pages/post.html',
        {
            # 'page_obj': page_obj,
        }
    )