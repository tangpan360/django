from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("你好，这是我的第一个Django视图！")

# def post_list(request):
#     """
#     显示所有已发布的文章列表
#     """
#     posts = Post.objects.filter(status='published')
#     return render(request, 'blog/post/list.html', {'posts': posts})


class PostListView(ListView):
    """
    显示所有已发布的文章列表

    ListView是Django提供的通用视图，用于显示对象列表
    它会自动为我们处理分页和上下文数据
    """
    # 指定要查阅的数据集
    queryset = Post.objects.filter(status='published')

    # 指定在模板中使用的上下文变量名，默认为'object_list'
    context_object_name = 'posts'

    # 指定要使用的模板，默认为'blog/post_list.html'
    template_name = 'blog/post/list.html'

    # 指定每页显示的对象数量
    paginate_by = 3


# def post_detail(request, year, month, day, slug):
#     """
#     显示单篇文章的详细内容
#     """
#     post = get_object_or_404(Post,
#                             slug=slug,
#                             status='published',
#                             publish__year=year,
#                             publish__month=month,
#                             publish__day=day)
#     # 获取文章的所有活动评论
#     comments = post.comments.filter(active=True)
#     return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments})


class PostDetailView(DetailView):
    """
    显示单篇文章的详细内容

    DetailView是Django提供的通用视图，用于显示单个对象的详细信息
    """
    # 指定要使用的模型
    model = Post

    # 指定在模板中使用的上下文变量名，默认为'object'
    context_object_name = 'post'

    # 指定要使用的模板，默认为'blog/post_detail.html'
    template_name = 'blog/post/detail.html'

    def get_queryset(self):
        """
        重写get_queryset方法，只返回已发布的文章
        """
        # 只获取已发布的文章
        return Post.objects.filter(status='published')
    
    def get_object(self):
        """
        重写get_object方法，使用年、月、日和slug获取文章对象
        """
        # 从URL参数中获取年、月、日和slug
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        slug = self.kwargs['slug']

        # 使用get_object_or_404函数获取对象，如果不存在则返回404错误
        return get_object_or_404(
            self.get_queryset(),
            publish__year=year,
            publish__month=month,
            publish__day=day,
            slug=slug,
        )
    
    def get_context_data(self, **kwargs):
        """
        重写get_context_data方法，添加评论到上下文
        """
        # 调用父类方法获取上下文
        context = super().get_context_data(**kwargs)
        # 添加文章的活动评论到上下文
        context['comments'] = self.object.comments.filter(active=True)
        return context
    

# 文章创建视图
class PostCreateView(LoginRequiredMixin, CreateView):
    """
    创建新文章的视图

    CreateView是Django提供的通用视图，用于创建对象
    LoginRequiredMixin确保只有登录用户才能访问此视图
    """
    # 指定要使用的视图
    model = Post

    # 指定要在表单中包含的字段
    fields = ['title', 'slug', 'category', 'body', 'status']

    # 指定要使用的模板
    template_name = 'blog/post/post_form.html'

    # 指定登录URL，当用户未登录时会重定向到此URL
    login_url = '/login/'

    def form_valid(self, form):
        """
        重写form_valid方法，在保存表单前设置作者
        """
        # 设置当前用户为文章作者
        form.instance.author = self.request.user
        # 调用父类方法保存表单
        return super().form_valid(form)

# 文字编辑视图
class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    编辑现有文章的视图

    UpdateView是Django提供的通用视图，用于更新对象
    LoginRequiredMixin确保只有登录用户才能访问此视图
    """
    # 指定要使用的模型
    model = Post

    # 指定要在表单中包含的字段
    fields = ['title', 'slug', 'category', 'body', 'status']

    # 指定要使用的模板，与创建视图共用一个模板
    template_name = 'blog/post/post_form.html'

    # 指定登录URL，当用户未登录时会重定向到此URL
    login_url = '/login/'

    def get_queryset(self):
        """
        重写get_queryset方法，确保用户只能编辑自己的文章
        """
        # 只返回当前用户创建的文章
        return Post.objects.filter(author=self.request.user)


# 文章删除视图
class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    删除文章的视图

    DeleteView是Django提供的通用视图，用于删除对象
    LoginRequiredMixin确保只有登录用户才能访问此视图
    """
    # 指定要使用的模型
    model = Post

    # 指定要使用的模板
    template_name = 'blog/post/post_confirm_delete.html'

    # 指定删除成功后的重定向URL
    # 使用reverse_lazy而不是reverse，因为URL配置在项目加载时可能还不可用
    success_url = reverse_lazy('blog:post_list')

    # 指定登录URL，当用户未登录时会重定向到此URL
    login_url = '/login/'

    def get_queryset(self):
        """
        重写get_query方法，确保用户只能删除自己的文章
        """
        # 只返回当前用户创建的文章
        return Post.objects.filter(author=self.request.user)