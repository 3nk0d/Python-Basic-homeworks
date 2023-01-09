from django.core.management.base import BaseCommand
from view_news.models import Posts, Users, Req_Urls, Tags


class Command (BaseCommand):
    help = 'Fill DB'

    def handle(self, *args, **options):
        Tags.objects.all().delete()
        Req_Urls.objects.all().delete()
        Users.objects.all().delete()
        Posts.objects.all().delete()


        user1 = Users.objects.create(username='Vovan3', name='Vova', email='Vova@email.com')
        user2 = Users.objects.create(username='Ivan12', name='Ivan', email='Ivan@email.com')
        user3 = Users.objects.create(username='Ann4', name='Anna', email='Anna@email.com')

        first_url = Req_Urls.objects.create(name='first', url='http://www.google.com')
        second_url = Req_Urls.objects.create(name='second', url='http://www.yandex.com')

        post1 = Posts.objects.create(title='Cool title 1', text='The best text 1', url='some url 1', from_url=first_url)
        # post1.from_url.add(first_url)
        # post1.save()
        # from_url1 = post1.from_url.all()
        # for item in from_url1:
        #     print(from_url1.name)
        post2 = Posts.objects.create(title='Cool title 2', text='The best text 2', url='some url 2', from_url=first_url)
        #post2.from_url.add(first_url)
        post3 = Posts.objects.create(title='Cool title 3', text='The best text 3', url='some url 3', from_url=second_url)
        #post3.from_url.add(second_url)
        post4 = Posts.objects.create(title='Cool title 4', text='The best text 4', url='some url 4', from_url=second_url)
        #post4.from_url.add(second_url)

        tag1 = Tags.objects.create(tag='найден')
        tag1.users.add(user1)
        tag2 = Tags.objects.create(tag='взломан')
        tag2.users.add(user2, user3)
        tag3 = Tags.objects.create(tag='авария')
        tag3.users.add(user3)
        tag4 = Tags.objects.create(tag='яндекс')
        tag4.users.add(user1, user3)
