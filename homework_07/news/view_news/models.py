from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=50)
    url = models.URLField()


class Users(models.Model):
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    email = models.EmailField()


class Req_Urls(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField()
