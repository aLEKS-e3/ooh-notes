from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from note.models import TechTag, Note, NoteGroup


class ModelsTest(TestCase):
    def setUp(self):
        self.tag = TechTag.objects.create(name="Ruby")
        self.user = get_user_model().objects.create_user(
            username="papajoe",
            password="$ecreT_550",
            skill=self.tag
        )
        self.note = Note.objects.create(
            title="Bibobus",
            body="Abubabububa",
            owner=self.user
        )
        self.note.tags.add(self.tag)

        self.group = NoteGroup.objects.create(
            name="NoHomoGroup",
            owner=self.user,
            tag=self.tag,
        )
        self.group.notes.add(self.note)

    def test_note_str_method(self):
        self.assertEqual(
            str(self.note),
            f"{self.note.title} by {self.note.owner.username}"
        )

    def test_note_get_absolute_url_method(self):
        url = reverse("note:note-detail", kwargs={"pk": self.note.pk})
        self.assertEqual(self.note.get_absolute_url(), url)

    def test_note_group_str_method(self):
        self.assertEqual(
            str(self.group),
            f"{self.group.name} by {self.group.owner.username}"
        )

    def test_note_group_get_absolute_url_method(self):
        url = reverse("note:note-group-detail", kwargs={"pk": self.group.pk})
        self.assertEqual(self.group.get_absolute_url(), url)

    def test_tech_tag_str_method(self):
        self.assertEqual(str(self.tag), self.tag.name)
