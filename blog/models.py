from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "草稿"),
        ("published", "已发布")
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("-publish",)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                    args=[self.publish.year,
                        self.publish.month,
                        self.publish.day,
                        self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
    
    class Meta:
        ordering = ("created",)


class Profile(models.Model):
    """
    用户个人资料模型

    与Django内置的User模型通过一对一关系关联
    存储用户的额外信息，如头像、个人简介等
    """
    # 一对一关联到Django内置的User模型
    # 当User被删除时，关联的Profile也会被删除（级联删除）
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 用户头像，可以为空
    # upload_to指定上传文件的存储路径
    avatar = models.ImageField(upload_to='profile_avatars/', null=True, blank=True)

    # 用户个人简介，可以为空
    bio = models.TextField(max_length=500, blank=True)

    # 用户网站，可以为空
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        """返回用户名作为对象的字符串表示"""
        return f'{self.user.username}的个人资料'
    
# 信号接收器：当创建新用户时自动创建对应的个人资料
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    当User模型保存时触发的信号接收器

    如果是新创建的用户，则自动创建一个关联的个人资料
    """
    if created:
        Profile.objects.create(user=instance)

# 信号接收器：当更新用户时同步更新个人资料
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    当User模型保存时触发的信号接收器

    确保用户的个人资料也被保存
    """
    instance.profile.save()