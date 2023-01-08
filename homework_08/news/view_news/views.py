from django.shortcuts import render
from django.views.generic import ListView, DetailView
from view_news.models import Posts


def main_page(request):
    return render(request, 'view_news/index.html')


def Posts_ListView(ListView):
    model = Posts
