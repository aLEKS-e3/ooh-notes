from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from note.forms import NoteSearchForm, NoteGroupSearchForm
from note.models import TechTag, Note, NoteGroup


class SearchFormsTest(TestCase):
    def setUp(self):
        self.tag = TechTag.objects.create(name="Ruby")
        self.user = get_user_model().objects.create_user(
            username="papajoe",
            password="$ecreT_550",
            skill=self.tag
        )
        self.client.force_login(self.user)

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

        self.group2 = NoteGroup.objects.create(
            name="Lips",
            owner=self.user,
            tag=self.tag,
        )
        self.group2.notes.add(self.note, self.note2)

        self.note_response = self.client.get(
            reverse("note:note-list"), {"title": "b"}
        )
        self.note_group_response = self.client.get(
            reverse("note:note-group-list"), {"name": "Li"}
        )

    @staticmethod
    def get_dict_search_form_with_field():
        return {
            NoteSearchForm: "title",
            NoteGroupSearchForm: "name"
        }

    def test_empty_search_form_is_valid(self):
        field_form = self.get_dict_search_form_with_field()
        for search_form, field in field_form.items():
            form_data = {
                field: "",
            }
            form = search_form(data=form_data)
            self.assertTrue(form.is_valid())

    def test_note_search_returns_expected_results(self):
        self.assertQuerysetEqual(
            self.note_response.context["note_list"],
            Note.objects.filter(title__icontains="b"),
        )

    def test_note_group_search_returns_expected_results(self):
        self.assertQuerysetEqual(
            self.note_group_response.context["note_group_list"],
            NoteGroup.objects.filter(name__icontains="Li"),
        )
