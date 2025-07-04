from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

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


class PostDetailView(FormMixin,DetailView):
    """
    显示单篇文章的详细内容，并处理评论提交

    FormMixin: 为DetailView添加表单处理功能
    DetailView是Django提供的通用视图，用于显示单个对象的详细信息
    """
    # 指定要使用的模型
    model = Post

    # 指定在模板中使用的上下文变量名，默认为'object'
    context_object_name = 'post'

    # 指定要使用的模板，默认为'blog/post_detail.html'
    template_name = 'blog/post/detail.html'

    # 指定要使用的表单类
    form_class = CommentForm

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
        # 添加评论表单到上下文
        context['comment_form'] = self.get_form()
        return context

    def get_success_url(self):
        """
        返回表单提交成功后的重定向URL
        """
        # 重定向回当前文章详情页
        return self.object.get_absolute_url()
    
    def post(self, request, *args, **kwargs):
        """
        处理POST请求，提交评论
        """
        # 获取当前文章对象
        self.object = self.get_object()
        # 获取表单实例
        form = self.get_form()

        # 验证表单数据
        if form.is_valid():
            # 处理有效的表单数据
            return self.form_valid(form)
        else:
            # 处理无效的表单数据
            return self.form_invalid(form)
        
    def form_valid(self, form):
        """
        处理有效的表单数据
        """
        # 创建评论对象，但不保存到数据库
        new_comment = form.save(commit=False)
        # 设置评论所属的文章
        new_comment.post = self.object
        # 保存评论到数据库
        new_comment.save()
        # 添加成功消息
        messages.success(self.request, "评论提交成功！")
        # 调用父类方法完成表单处理
        return super().form_valid(form)


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


class RegisterView(CreateView):
    """
    用户注册视图

    使用CreateView通用视图处理用户注册
    """
    # 指定使用的表单类
    form_class = UserRegistrationForm
    # 指定模板
    template_name = 'registration/register.html'
    # 注册成功后重定向到博客首页
    success_url = reverse_lazy('blog:post_list')

    # 表单有效时的处理
    def form_valid(self, form):
        # 保存用户
        user = form.save()
        # 自动登录新注册的用户
        login(self.request, user)
        return super().form_valid(form)
    
@login_required
def profile(request):
    """
    用户个人资料视图

    显示和更新用户的个人资料
    需要用户登录才能访问（由login_required装饰器保证
    """
    # 如果是POST请求，处理表单提交
    if request.method == 'POST':
        # 创建表单实例并填充当前用户数据
        user_form = UserUpdateForm(request.POST, instance=request.user)
        # 创建个人资料表单实例，包括文件上传
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
            )
        
        # 验证表单
        if user_form.is_valid() and profile_form.is_valid():
            # 保存表单数据
            user_form.save()
            profile_form.save()
            # 添加成功消息
            messages.success(request, '您的个人资料已更新！')
            # 重定向到个人资料页面
            return redirect('profile')
    
    else:
        # GET请求，创建表单实例并填充当前用户数据
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    # 准备上下文数据
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    # 渲染模板
    return render(request, 'blog/profile.html', context)