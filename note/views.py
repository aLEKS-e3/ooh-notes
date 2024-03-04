from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from note.models import Note


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "note/index.html")


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "note/note_list.html"
    paginate_by = 5


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
