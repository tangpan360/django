from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("你好，这是我的第一个Django视图！")

def post_list(request):
    """
    显示所有已发布的文章列表
    """
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, slug):
    """
    显示单篇文章的详细内容
    """
    post = get_object_or_404(Post,
                            slug=slug,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    # 获取文章的所有活动评论
    comments = post.comments.filter(active=True)
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments})