from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.username} : {self.email}'


class Req_Urls(models.Model):
    name = models.CharField(max_length=40, unique=True)
    url = models.URLField()

    def __str__(self):
        return f'{self.name} : {self.url}'


class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    url = models.URLField()
    from_url = models.ForeignKey(Req_Urls, on_delete=models.PROTECT)


class Tags(models.Model):
    tag = models.CharField(max_length=50, blank=False, unique=True)
    users = models.ManyToManyField(Users)
