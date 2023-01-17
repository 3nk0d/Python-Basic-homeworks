from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from view_news.models import Posts, Users, Req_Urls, Tags
from django.urls import reverse_lazy


def main_page(request):
    return render(request, 'view_news/index.html')


class Posts_CreateView(CreateView):
    model = Posts

class Posts_ListView(ListView):
    model = Posts


class Posts_DetailView(DetailView):
    model = Posts


class Posts_Delete(DeleteView):
    model = Posts
    success_url = reverse_lazy('posts')


class Users_CreateView(CreateView):
    model = Users


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


class Req_Urls_DetailView(DetailView):
    model = Req_Urls


class Req_Urls_Delete(DeleteView):
    model = Req_Urls
    success_url = reverse_lazy('sources')


class Tags_CreateView(CreateView):
    model = Tags


class Tags_ListView(ListView):
    model = Tags


class Tags_DetailView(DetailView):
    model = Tags


class Tags_Delete(DeleteView):
    model = Tags
    success_url = reverse_lazy('tags')