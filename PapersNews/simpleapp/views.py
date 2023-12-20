from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForm
from .models import Post


class NewsList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = '-time_in'
    paginate_by = 5

class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class NewsCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    context_object_name = 'posts'

class NewsUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(type='NW').order_by('-time_in')
        return posts

class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'posts'
    succes_url = reverse_lazy('post_list')


class ArticleCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'article_create.html'
    context_object_name = 'posts'

class ArticleUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'article_edit.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(type='AR').order_by('-time_in')
        return posts

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'arcticle_delete.html'
    context_object_name = 'posts'
    succes_url = reverse_lazy('post_list')


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post_search'
    ordering = ['-time_in']
    paginate_by = 10
    filter_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=queryset)
        return self.filter.qs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        context['list_in_page'] = self.paginate_by
        context['all_posts'] = Post.objects.all()
        return context