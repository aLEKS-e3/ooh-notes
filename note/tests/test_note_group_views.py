from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from note.models import Note, TechTag, NoteGroup

NOTE_GROUP_PK = 1
NOTE_GROUP_LIST_URL = reverse("note:note-group-list")
NOTE_GROUP_DETAIL_URL = reverse(
    "note:note-group-detail",
    kwargs={"pk": NOTE_GROUP_PK}
)


class PublicNoteGroupViewsTest(TestCase):
    def test_login_required(self):
        for url in [NOTE_GROUP_LIST_URL, NOTE_GROUP_DETAIL_URL]:
            response = self.client.get(url)
            self.assertNotEqual(response.status_code, 200)


class PrivateNoteGroupViewsTest(TestCase):
    def setUp(self):
        self.tag = TechTag.objects.create(name="Machine Learning")
        self.user = get_user_model().objects.create_user(
            username="papajoe",
            password="$ecreT_550",
            skill=self.tag
        )
        self.client.force_login(self.user)

        self.user2 = get_user_model().objects.create_user(
            username="DadMad",
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

        self.group = NoteGroup.objects.create(
            name="NoHomoGroup",
            owner=self.user,
            tag=self.tag,
        )
        self.group.notes.add(self.note, self.note2)

    def test_note_group_list_url_response(self):
        response = self.client.get(NOTE_GROUP_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "note/note_group_list.html")

    def test_note_group_list_has_groups(self):
        response = self.client.get(NOTE_GROUP_LIST_URL)
        groups = NoteGroup.objects.all()
        self.assertEqual(
            list(response.context["note_group_list"]),
            list(groups)
        )

    def test_note_group_search_form_exists(self):
        response = self.client.get(NOTE_GROUP_LIST_URL)
        self.assertContains(response, "Search by name")

    def test_note_group_filter_form_exists(self):
        response = self.client.get(NOTE_GROUP_LIST_URL)
        self.assertContains(response, "Apply filter")

    def test_note_detail_view_shows_relation_fields(self):
        response = self.client.get(NOTE_GROUP_DETAIL_URL)
        page_content = response.content.decode("utf-8")

        self.assertIn(str(self.user), page_content)
        notes = self.group.notes.values_list("title", flat=True)
        self.assertTrue(all(title in page_content for title in notes))

    def test_can_not_update_or_delete_another_group(self):
        self.client.force_login(self.user2)
        response = self.client.get(NOTE_GROUP_DETAIL_URL + "/update/")
        self.assertEqual(response.status_code, 404)

        response = self.client.get(NOTE_GROUP_DETAIL_URL + "/delete/")
        self.assertEqual(response.status_code, 404)
