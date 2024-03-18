from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from note.models import TechTag


class UsersModelsTest(TestCase):
    def setUp(self):
        self.tag = TechTag.objects.create(name="Ruby")
        self.user = get_user_model().objects.create_user(
            username="papajoe",
            password="$ecreT_550",
            skill=self.tag
        )

    def test_tech_user_str_method(self):
        self.assertEqual(
            str(self.user),
            self.user.username
        )

    def test_tech_user_get_absolute_url_method(self):
        url = reverse("users:profile", kwargs={"pk": self.user.pk})
        self.assertEqual(self.user.get_absolute_url(), url)
