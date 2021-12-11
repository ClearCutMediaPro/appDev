from typing import Text
from django.db import models
from django.views.generic import ListView,DetailView,TemplateView

from .models import Post

from django.contrib import messages # import messages from django.contrib


class feedPageView(TemplateView):
    http_method_names = ['get']
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts'  
    queryset = Post.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')[0:1] # Django get all of the posts and order them by their id descending
        return context

class feedDetailView(DetailView):
    template_name='detail.html'
    model=Post