"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from view_news.views import main_page, Posts_ListView, Users_ListView, Req_Urls_ListView, Tags_ListView, Posts_DetailView, Users_DetailView, Req_Urls_DetailView, Tags_DetailView

urlpatterns = [
    path('', main_page, name='main'),
    path('posts/', Posts_ListView.as_view(), name='posts'),
    path('posts/<int:pk>/', Posts_DetailView.as_view(), name='post'),
    path('users/', Users_ListView.as_view(), name='users'),
    path('users/<int:pk>/', Users_DetailView.as_view(), name='user'),
    path('req_urls/', Req_Urls_ListView.as_view(), name='sources'),
    path('req_urls/<int:pk>/', Req_Urls_DetailView.as_view(), name='source'),
    path('tags/', Tags_ListView.as_view(), name='tags'),
    path('tags/<int:pk>/', Tags_DetailView.as_view(), name='tag'),
    path('admin/', admin.site.urls),
]
