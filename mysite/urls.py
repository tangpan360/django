"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # 导入HttpResponse
from django.contrib.auth import views as auth_views
from blog.views import RegisterView, profile
from django.conf import settings
from django.conf.urls.static import static

# 创建一个简单的根路径视图函数
def home(request):
    return HttpResponse("欢迎来到我的Django网站首页！<br><a href='/blog/'>访问博客</a>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', home, name='home'),  # 添加根路径URL模式

    # 登录和退出URL
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # 注册URL
    path('register/', RegisterView.as_view(), name='register'),

    # 密码重置视图 - 输入邮箱的表单页面
    path('password_reset/',
        auth_views.PasswordResetView.as_view(
            # 指定使用的模板
            template_name='registration/password_reset_form.html',
            # 指定邮件主题模板
            subject_template_name='registration/password_reset_subject.txt',
            # 指定邮件内容模板
            email_template_name='registration/password_reset_email.html',
            # 成功后重定向的URL名称
            success_url='/password_reset/done/'
        ),
        name='password_reset'),
    # 密码重置邮件发送成功页面
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'),

    # 密码重置确认页面
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            success_url='/reset/done/'
        ),
        name='password_reset_confirm'),

    # 密码重置完成页面
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'),

    path('profile/', profile, name='profile'),
]

# 仅在开发环境中添加没提文件URL配置
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)