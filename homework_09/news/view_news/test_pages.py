from django.test import TestCase


class TestPage(TestCase):

    def setUp(self) -> None:
        response = self.client.post("/users/create/", {"username": "dwad", "name": "wadw", "email": "dawd32dwa.com"})
        self.assertEqual(response.status_code, 200)

    def test_pages(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/tags/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/req_urls/")
        self.assertEqual(response.status_code, 200)

    def test_data_pages(self) -> None:
        response = self.client.get("/users/1/")
        self.assertEqual(response.status_code, 200)
