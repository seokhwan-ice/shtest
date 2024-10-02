from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render
# from .models import Gallery
from django.http import JsonResponse


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def index(request):
    return render(request, 'gallery/index.html')


def get_post(request):
    databases = ['default', 'postgres'] ##, 'mysql'
    for db in databases:
        try:
            # 기본적으로 'default'에서 먼저 시도
            posts = Post.objects.using(db).all()
            if posts.exists():
                return JsonResponse({'posts': list(posts.values())})
        except Exception as e:
            # 읽기에 실패하면 다음 데이터베이스로 넘어감
            print(f"Failed to read from database {db}: {e}")
            continue
    return JsonResponse({'error': 'No data found in any database'}, status=404)

