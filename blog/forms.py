from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    """
    评论表单类

    使用ModelForm可以自动根据模型生成表单字段
    """

    class Meta:
        # 指定表单关联的模型
        model = Comment
        # 指定表单包含的字段
        fields = ['name', 'email', 'body']

        # 自定义字段的小部件（widget）属性
        widgets = {
            # 为name字段添加CSS类和占位符
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入您的名字',
            }),
            # 为email字段添加CSS类和占位符
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入您的邮箱',
            }),
            # 为body字段添加CSS类、占位符和行数
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '请输入您的评论',
                'rows': 5,
            }),
        }


# 自定义用户注册表单，集成Django内置的UserCreationForm
class UserRegistrationForm(UserCreationForm):
    """
    用户注册表单

    扩展Django内置的UserCreationForm，添加email字段
    UserCreationForm默认包含username、password1和password2字段
    """
    # 添加email字段，并设置为必填
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={
                                'class': 'form-control',
                                'placeholder': '请输入您的邮箱',
                            }))

    # 自定义字段的widget属性
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为username字段添加样式
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '请输入用户名',
        })
        # 为password1字段添加样式
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '请输入密码',
        })
        # 为password2字段添加样式
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '请确认密码',
        })

    class Meta:
        model = User  # 关联到Django内置的User模型
        # 指定表单包含的字段
        fields = ['username', 'email', 'password1', 'password2']

    # 保存用户时同时保存email
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user