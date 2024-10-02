from django.urls import path
from .views import PostListCreateView, PostDetailView
from . import views

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('', views.index, name='index'),
]
