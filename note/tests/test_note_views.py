from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from note.models import Note, TechTag

NOTE_PK = 1
NOTE_LIST_URL = reverse("note:note-list")
NOTE_DETAIL_URL = reverse("note:note-detail", kwargs={"pk": NOTE_PK})


class PublicNoteViewsTest(TestCase):
    def test_login_required(self):
        for url in [NOTE_DETAIL_URL, NOTE_LIST_URL]:
            response = self.client.get(url)
            self.assertNotEqual(response.status_code, 200)


class PrivateNoteViewsTest(TestCase):
    def setUp(self):
        self.tag = TechTag.objects.create(name="Ruby")
        self.user = get_user_model().objects.create_user(
            username="papajoe",
            password="$ecreT_550",
            skill=self.tag
        )
        self.client.force_login(self.user)

        self.user2 = get_user_model().objects.create_user(
            username="Magamed",
            password="$ecreT_550",
            skill=self.tag
        )

        self.note = Note.objects.create(
            title="Papajoe",
            body="Lorem ipsum dolor",
            owner=self.user,
        )
        self.note2 = Note.objects.create(
            title="Bloobobo",
            body="Lorem ipsum dolor",
            owner=self.user,
        )

        self.note.tags.add(self.tag)
        self.note2.tags.add(self.tag)

    def test_note_list_url_response(self):
        response = self.client.get(NOTE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "note/note_list.html")

    def test_note_list_has_notes(self):
        response = self.client.get(NOTE_LIST_URL)
        notes = Note.objects.all()
        self.assertEqual(
            list(response.context["note_list"]),
            list(notes)
        )

    def test_note_search_form_exists(self):
        response = self.client.get(NOTE_LIST_URL)
        self.assertContains(response, "Search by title")

    def test_note_filter_form_exists(self):
        response = self.client.get(NOTE_LIST_URL)
        self.assertContains(response, "Apply filter")

    def test_note_detail_view_shows_relation_fields(self):
        response = self.client.get(NOTE_DETAIL_URL)
        page_content = response.content.decode("utf-8")

        self.assertIn(str(self.user), page_content)
        tags = self.note.tags.values_list("name", flat=True)
        self.assertTrue(all(tag in page_content for tag in tags))

    def test_note_detail_view_shows_content(self):
        response = self.client.get(NOTE_DETAIL_URL)
        page_content = response.content.decode("utf")
        self.assertIn(str(self.note.body), page_content)

    def test_can_not_update_or_delete_another_note(self):
        self.client.force_login(self.user2)
        response = self.client.get(NOTE_DETAIL_URL + "/update/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(NOTE_DETAIL_URL + "/delete/")
        self.assertEqual(response.status_code, 404)
