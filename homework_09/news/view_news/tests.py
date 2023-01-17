from django.test import TestCase
from .models import Users, Req_Urls, Posts, Tags
# Create your tests here.

class TestUsers(TestCase):

    def setUp(self) -> None:
        self.user = Users.objects.create(username="link", name="James", email="Jam2@mail.com")

    def tearDown(self) -> None:


    def CheckData(self):
        self.assertEqual(self.user.username, "link")
        self.assertEqual(self.user.name, "James")
        self.assertEqual(self.user.email, "Jam2@mail.com")

