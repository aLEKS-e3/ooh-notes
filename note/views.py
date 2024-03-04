from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from note.forms import NoteCreationForm
from note.models import Note


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
    form_class = NoteCreationForm
    success_url = reverse_lazy("note:note-list")


class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    form_class = NoteCreationForm
    success_url = reverse_lazy("note:note-list")


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    success_url = reverse_lazy("taxi:car-list")
