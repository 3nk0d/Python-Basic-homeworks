from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from view_news.models import Posts, Users, Req_Urls, Tags
from django.urls import reverse_lazy
from .forms import PostForm

def main_page(request):
    return render(request, 'view_news/index.html')


class Posts_CreateView(CreateView):
    model = Posts
    fields = ('title', 'text', 'url', 'from_url')
    #form_class = PostForm
    success_url = reverse_lazy('posts')


class Posts_ListView(ListView):
    model = Posts


class Posts_DetailView(DetailView):
    model = Posts


class Posts_Delete(DeleteView):
    model = Posts
    success_url = reverse_lazy('posts')


class Users_CreateView(CreateView):
    model = Users
    fields = ('username', 'name', 'email')
    success_url = reverse_lazy('users')


class Users_ListView(ListView):
    model = Users


class Users_DetailView(DetailView):
    model = Users


class Users_Delete(DeleteView):
    model = Users
    success_url = reverse_lazy('users')


class Req_Urls_ListView(ListView):
    model = Req_Urls


class Req_Urls_CreateView(CreateView):
    model = Req_Urls
    fields = ('name', 'url')
    success_url = reverse_lazy('sources')


class Req_Urls_DetailView(DetailView):
    model = Req_Urls


class Req_Urls_Delete(DeleteView):
    model = Req_Urls
    success_url = reverse_lazy('sources')


class Tags_CreateView(CreateView):
    model = Tags
    fields = ('tag', 'users')
    success_url = reverse_lazy('tags')


class Tags_ListView(ListView):
    model = Tags


class Tags_DetailView(DetailView):
    model = Tags


class Tags_Delete(DeleteView):
    model = Tags
    success_url = reverse_lazy('tags')


class Posts_UpdateView(UpdateView):
    model = Posts
    fields = ('title', 'text', 'url', 'from_url')
    #form_class = PostForm
    success_url = reverse_lazy('posts')


class Users_UpdateView(UpdateView):
    model = Users
    fields = ('username', 'name', 'email')
    success_url = reverse_lazy('users')

class Req_Urls_UpdateView(UpdateView):
    model = Req_Urls
    fields = ('name', 'url')
    success_url = reverse_lazy('sources')

class Tags_UpdateView(UpdateView):
    model = Tags
    fields = ('tag', 'users')
    success_url = reverse_lazy('tags')