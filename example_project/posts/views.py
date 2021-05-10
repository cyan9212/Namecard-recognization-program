from django.shortcuts import render
from .models import Post
from .models import uploadPost
from .forms import PostForm
from .forms import uploadPostForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class UploadHomePostView(ListView):
    model = uploadPost
    template_name = 'uploadhome.html'

class UploadCreatePostView(CreateView):
    model = uploadPost
    form_class = uploadPostForm
    template_name = 'uploadcreate.html'
    success_url = reverse_lazy('uploadhome')
