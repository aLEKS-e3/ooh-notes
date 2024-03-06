from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from note.models import TechTag, Note, NoteGroup

USER_PK = 1
USER_PROFILE_URL = reverse("users:profile", kwargs={"pk": USER_PK})


class PublicTechUserViewsTest(TestCase):
    def test_login_for_profile_required(self):
        response = self.client.get(USER_PROFILE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTechUserViewsTest(TestCase):
    def setUp(self):
        self.tag = TechTag.objects.create(name="")
        self.user = get_user_model().objects.create_user(
            username="papajoe",
            password="$ecreT_550",
            skill=self.tag
        )
        self.client.force_login(self.user)

        self.user2 = get_user_model().objects.create_user(
            username="papabob",
            password="$ecreT_550",
            skill=self.tag
        )
        self.note = Note.objects.create(
            title="Papajoe",
            body="Lorem ipsum dolor",
            owner=self.user,
        )
        self.note.tags.add(self.tag)

        self.group = NoteGroup.objects.create(
            name="NoHomoGroup",
            owner=self.user,
            tag=self.tag,
        )
        self.group.notes.add(self.note)

    def test_profile_url_response(self):
        response = self.client.get(USER_PROFILE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/tech_user_detail.html")

    def test_profile_has_personal_info(self):
        response = self.client.get(USER_PROFILE_URL)
        page_content = response.content.decode("utf-8")

        self.assertIn(self.user.username, page_content)
        self.assertIn(self.user.email, page_content)

    def test_profile_has_groups_nad_notes(self):
        response = self.client.get(USER_PROFILE_URL)
        page_content = response.content.decode("utf-8")

        groups = self.user.groups.values_list("name", flat=True)
        notes = self.user.notes.values_list("title", flat=True)

        self.assertTrue(all(title in page_content for title in notes))
        self.assertTrue(all(group in page_content for group in groups))

    def test_can_not_update_or_delete_another_profile(self):
        self.client.force_login(self.user2)
        response = self.client.get(USER_PROFILE_URL + "/update/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(USER_PROFILE_URL + "/delete/")
        self.assertEqual(response.status_code, 404)
