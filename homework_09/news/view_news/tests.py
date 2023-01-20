from django.test import TestCase
from .models import Users, Req_Urls, Posts, Tags


# Create your tests here.

class TestData(TestCase):

    def setUp(self) -> None:
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

    def test_created_user_data(self):
        print("test_created_user_data")
        self.assertEqual(self.user.username, "link")
        self.assertEqual(self.user.name, "James")
        self.assertEqual(self.user.email, "Jam2@mail.com")

    def test_update_user_data(self):
        print("test_update_user_data")
        self.user.username = "MkK1ddy"
        self.user.name = "Mike"
        self.user.email = "MkK1ddy@mail.org"
        self.assertEqual(self.user.username, "MkK1ddy")
        self.assertEqual(self.user.name, "Mike")
        self.assertEqual(self.user.email, "MkK1ddy@mail.org")

    def test_created_Req_Urls_data(self):
        print("test_created_Req_Urls_data")
        self.assertEqual(self.url.name, "Dzen")
        self.assertEqual(self.url.url, "https://dzen.ru/news?issue_tld=ru")

    def test_update_Req_Urls_data(self):
        print("test_update_Req_Urls_data")
        self.url.name = "BBC"
        self.url.url = "https://www.bbc.co.uk/"
        self.assertEqual(self.url.name, "BBC")
        self.assertEqual(self.url.url, "https://www.bbc.co.uk/")

    def test_created_tag_data(self):
        print("test_created_tag_data")
        self.assertEqual(self.tag.tag, "landscapes")
        print(self.tag.users.all())
        for item in self.tag.users.all():
            self.assertEqual(item.username, "link")


    def test_update_tag_data(self):
        print("test_update_tag_data")
        self.tag.tag = "lake"
        user1 = Users.objects.create(username="pol3x", name="Polly", email="Polly67@mail.com")
        self.tag.users.add(user1)
        self.assertEqual(self.tag.tag, "lake")
        for item in self.tag.users.all():
            if item.username == "link":
                self.assertEqual(item.username, "link")
                continue
            self.assertEqual(item.username, "pol3x")
        Users.objects.filter(username="pol3x").delete()

    def test_created_post_data(self):
        print("test_created_post_data")
        self.assertEqual(self.post.title, self.title)
        self.assertEqual(self.post.text, self.text)
        self.assertEqual(self.post.url, self.post_url)
        self.assertEqual(self.post.from_url, self.url)

    def test_update_user_data(self):
        print("test_update_post_data")
        self.user.username = "MkK1ddy"
        self.user.name = "Mike"
        self.user.email = "MkK1ddy@mail.org"
        self.assertEqual(self.user.username, "MkK1ddy")
        self.assertEqual(self.user.name, "Mike")
        self.assertEqual(self.user.email, "MkK1ddy@mail.org")
