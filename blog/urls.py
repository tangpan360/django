from django.urls import path
from . import views


app_name = 'blog'  # 应用命名空间

urlpatterns = [
    # path('', views.index, name='index'),
    # 文章列表视图
    path('', views.post_list, name='post_list'),
    # 文章详情视图
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.post_detail,
        name='post_detail'),
]