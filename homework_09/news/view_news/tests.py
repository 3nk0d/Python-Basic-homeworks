from django.test import TestCase
from .models import Users, Req_Urls, Posts, Tags


# Create your tests here.

class TestData(TestCase):

    def setUp(self) -> None:
        self.user = Users.objects.create(username="link", name="James", email="Jam2@mail.com")
        print("Created:", self.user)
        self.url = Req_Urls.objects.create(name='dzen', url='https://dzen.ru/news?issue_tld=ru')

        self.title = 'How this photographer makes sublime landscapes of the American West'
        text = "The British visual artist, now based in Chicago, has become known for his sublime imagery of " \
               "remote landscapes using drone lighting, enhancing craggy peaks with halos, or writing glyphs in " \
               "the sky like signals from a supernatural entity. But for a long time, art was just a passion project " \
               "while he focused on a music career as one of the four members of the synth-pop band Ladytron."
        url = "https://edition.cnn.com/style/article/reuben-wu-landscape-photography/index.html"
        self.post = Posts.objects.create(title=self.title, text=text, url=url, from_url=self.url)

        self.tag = Tags.objects.create(tag='landscapes')
        self.tag.users.add(self.user)

    def tearDown(self) -> None:
        Users.objects.filter(username="link").delete()
        print("Deleted:", Users.objects.all())

        Posts.objects.filter(title=self.title).delete()

        Req_Urls.objects.filter(name="dzen").delete()

        Tags.objects.filter(tag='landscapes').delete()

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



