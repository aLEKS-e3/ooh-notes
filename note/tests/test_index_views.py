from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from note.models import TechTag

INDEX_URL = reverse("note:index")


class PublicIndexViewTests(TestCase):
    def test_index_view_anonymous(self):
        response = self.client.get(INDEX_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "note/landing.html")


class PrivateIndexViewTest(TestCase):
    def setUp(self):
        self.tag = TechTag.objects.create(name="Ruby")
        self.user = get_user_model().objects.create_user(
            username="papajoe",
            password="$ecreT_550",
            skill=self.tag
        )
        self.client.force_login(self.user)

    def test_index_response_logged_in(self):
        response = self.client.get(INDEX_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "note/index.html")
