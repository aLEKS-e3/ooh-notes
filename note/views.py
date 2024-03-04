from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from note.forms import NoteForm, NoteGroupForm
from note.models import Note, NoteGroup


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "note/index.html")


class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    template_name = "note/note_list.html"
    paginate_by = 5


class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note


class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("note:note-list")


class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    form_class = NoteForm


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    success_url = reverse_lazy("note:note-list")


class NoteGroupListView(LoginRequiredMixin, generic.ListView):
    model = NoteGroup
    context_object_name = "note_group_list"
    template_name = "note/note_group_list.html"
    paginate_by = 5


class NoteGroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = NoteGroup
    context_object_name = "note_group"
    template_name = "note/note_group_detail.html"


class NoteGroupCreateView(LoginRequiredMixin, generic.CreateView):
    model = NoteGroup
    form_class = NoteGroupForm
    template_name = "note/note_group_form.html"
    success_url = reverse_lazy("note:note-group-list")


class NoteGroupUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = NoteGroup
    form_class = NoteGroupForm
    template_name = "note/note_group_form.html"


class NoteGroupDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = NoteGroup
    template_name = "note/note_group_confirm_delete.html"
    success_url = reverse_lazy("note:note-group-list")
