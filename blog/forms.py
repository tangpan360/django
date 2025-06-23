from django import forms
from .models import Comment


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