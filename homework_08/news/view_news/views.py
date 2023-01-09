from django.shortcuts import render
from django.views.generic import ListView, DetailView
from view_news.models import Posts, Users, Req_Urls, Tags


def main_page(request):
    return render(request, 'view_news/index.html')


class Posts_ListView(ListView):
    model = Posts


class Posts_DetailView(DetailView):
    model = Posts


class Users_ListView(ListView):
    model = Users


class Users_DetailView(DetailView):
    model = Users


class Req_Urls_ListView(ListView):
    model = Req_Urls


class Req_Urls_DetailView(DetailView):
    model = Req_Urls


class Tags_ListView(ListView):
    model = Tags


class Tags_DetailView(DetailView):
    model = Tags