from django.template.loader import get_template 
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
from .models import Post
from rest_framework import generics
from .serializers import UserSerializer
# Create your views here.

def homepage(request):     
    template = get_template('index.html') #獲取網頁要貼文的網頁
    posts = Post.objects.all() #獲取 models.py底下的資料
    now = datetime.now() #現在時間
    html = template.render(locals()) #渲染成 html 
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

class UserList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = UserSerializer