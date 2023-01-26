from django.test import TestCase
from django.urls import reverse

from .models import Users, Req_Urls, Posts, Tags


class TestPage(TestCase):

    def setUp(self) -> None:
        # data = {"username": "dwad", "name": "wadw", "email": "dawd32dwa.com"}
        # response = self.client.post("/users/create/", data=data)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(Users.objects.count(), 1)


        self.user = Users.objects.create(username="link", name="James", email="Jam2@mail.com")
        print("Created:", self.user)

        self.url = Req_Urls.objects.create(name="Dzen", url="https://dzen.ru/news?issue_tld=ru")
        print("Created:", self.url)

        self.title = "How this photographer makes sublime landscapes of the American West"
        self.text = "The British visual artist, now based in Chicago, has become known for his sublime imagery of " \
                    "remote landscapes using drone lighting, enhancing craggy peaks with halos, or writing glyphs in " \
                    "the sky like signals from a supernatural entity. But for a long time, art was just a passion project " \
                    "while he focused on a music career as one of the four members of the synth-pop band Ladytron."
        self.post_url = "https://edition.cnn.com/style/article/reuben-wu-landscape-photography/index.html"
        self.post = Posts.objects.create(title=self.title, text=self.text, url=self.post_url, from_url=self.url)
        print("Created:", self.post)

        self.tag = Tags.objects.create(tag="landscapes")
        self.tag.users.add(self.user)
        self.tag.save()
        print("Created:", self.tag)

    def tearDown(self) -> None:
        Users.objects.filter(username="link").delete()
        print("Deleted:", Users.objects.all())

        Posts.objects.filter(title=self.title).delete()
        print("Deleted:", Posts.objects.all())

        Req_Urls.objects.filter(name="Dzen").delete()
        print("Deleted:", Req_Urls.objects.all())

        Tags.objects.filter(tag='landscapes').delete()
        print("Deleted:", Tags.objects.all())

    def test_pages(self) -> None:
        print("test_pages")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

        for item in response.context["object_list"]:
            self.assertEqual(item.username, self.user.username)
            self.assertEqual(item.name, self.user.name)
            self.assertEqual(item.email, self.user.email)

        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)

        for item in response.context["object_list"]:
            self.assertEqual(item.title, self.post.title)
            self.assertEqual(item.text, self.post.text)
            self.assertEqual(item.url, self.post.url)
            self.assertEqual(item.from_url, self.post.from_url)


        response = self.client.get("/tags/")
        self.assertEqual(response.status_code, 200)

        for item in response.context["object_list"]:
            self.assertEqual(item.tag, self.tag.tag)
            self.assertEqual(item.users, self.tag.users)

        response = self.client.get("/req_urls/")
        self.assertEqual(response.status_code, 200)

        for item in response.context["object_list"]:
            self.assertEqual(item.name, self.url.name)
            self.assertEqual(item.url, self.url.url)

        response = self.client.get("/no_page/")
        self.assertEqual(response.status_code, 404)

    def test_data_pages(self) -> None:
        print("test_data_pages")
        response = self.client.get(f"/users/{self.user.pk}/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["object"].username, self.user.username)
        self.assertEqual(response.context["object"].name, self.user.name)
        self.assertEqual(response.context["object"].email, self.user.email)

        response = self.client.get("/users/600/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"/req_urls/{self.url.pk}/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["object"].name, self.url.name)
        self.assertEqual(response.context["object"].url, self.url.url)

        response = self.client.get("/req_urls/600/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"/posts/{self.post.pk}/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["object"].title, self.post.title)
        self.assertEqual(response.context["object"].text, self.post.text)
        self.assertEqual(response.context["object"].url, self.post.url)
        self.assertEqual(response.context["object"].from_url, self.post.from_url)

        response = self.client.get(f"/posts/600/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"/tags/{self.tag.pk}/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["object"].tag, self.tag.tag)
        self.assertEqual(response.context["object"].users, self.tag.users)

        response = self.client.get("/tags/600/")
        self.assertEqual(response.status_code, 404)

    def test_create_pages(self) -> None:
        print("test_update_pages")
        response = self.client.get(f"/users/create/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/req_urls/create/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/posts/create/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/tags/create/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/no_page/create/")
        self.assertEqual(response.status_code, 404)

    def test_update_pages(self) -> None:
        print("test_update_pages")
        response = self.client.get(f"/users/change/{self.user.pk}/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["object"].username, self.user.username)
        self.assertEqual(response.context["object"].name, self.user.name)
        self.assertEqual(response.context["object"].email, self.user.email)

        response = self.client.get("/users/change/600/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"/req_urls/change/{self.url.pk}/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["object"].name, self.url.name)
        self.assertEqual(response.context["object"].url, self.url.url)

        response = self.client.get("/req_urls/change/600/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"/posts/change/{self.post.pk}/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["object"].title, self.post.title)
        self.assertEqual(response.context["object"].text, self.post.text)
        self.assertEqual(response.context["object"].url, self.post.url)
        self.assertEqual(response.context["object"].from_url, self.post.from_url)

        response = self.client.get(f"/posts/change/600/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"/tags/change/{self.tag.pk}/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["object"].tag, self.tag.tag)
        self.assertEqual(response.context["object"].users, self.tag.users)

        response = self.client.get("/tags/change/600/")
        self.assertEqual(response.status_code, 404)

    def test_delete_pages(self) -> None:
        print("test_pages")
        response = self.client.get(f"/users/delete/{self.user.pk}/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/users/delete/600/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"/req_urls/delete/{self.url.pk}/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/req_urls/delete/600/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"/posts/delete/{self.post.pk}/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/tags/delete/600/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f"/tags/delete/{self.tag.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_try_update_data(self):
        print("test_try_update_data")
        print(self.user.name)
        data = {"username": "link", "name": "Mike", "email": "Jam2@mail.com"}
        response = self.client.post(reverse("user_change", kwargs={'pk': self.user.id}), data=data)
        self.assertEqual(response.status_code, 302)
        print(self.user.name)

