from django.urls import path
from . import views


app_name = 'blog'  # 应用命名空间

urlpatterns = [
    # path('', views.index, name='index'),
    # # 文章列表视图
    # path('', views.post_list, name='post_list'),
    # 使用基于类的视图，as_view()方法将类转换为可调用的视图函数
    path('', views.PostListView.as_view(), name='post_list'),
    # # 文章详情视图
    # path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
    #     views.post_detail,
    #     name='post_detail'),
    # 使用基于类的文章详情视图
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.PostDetailView.as_view(),
        name='post_detail'),

    # 文章创建、编辑和删除视图
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]