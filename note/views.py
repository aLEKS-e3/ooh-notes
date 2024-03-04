from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from note.forms import NoteForm, NoteGroupForm, NoteSearchForm, NoteGroupSearchForm, TechTagFilterForm
from note.models import Note, NoteGroup


def index(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return render(request, "note/index.html")
    return render(request, "note/landing.html")


class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    template_name = "note/note_list.html"
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        queryset = Note.objects.all()
        form = NoteSearchForm(self.request.GET)
        tag = TechTagFilterForm(self.request.GET)

        if form.is_valid():
            queryset = queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )
        if tag.is_valid():
            if tag.cleaned_data["tag"]:
                queryset = queryset.filter(
                    tags=tag.cleaned_data["tag"]
                )

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(NoteListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        tag = self.request.GET.get("tag", "")

        context["search_form"] = NoteSearchForm(
            initial={"title": title}
        )
        context["filter_form"] = TechTagFilterForm(
            initial={"tag": tag}
        )
        return context


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

    def get_queryset(self) -> QuerySet:
        queryset = NoteGroup.objects.all()
        form = NoteGroupSearchForm(self.request.GET)
        tag = TechTagFilterForm(self.request.GET)

        if tag.is_valid():
            if tag.cleaned_data["tag"]:
                queryset = queryset.filter(
                    tag__name=tag.cleaned_data["tag"]
                )

        if form.is_valid():
            queryset = queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(NoteGroupListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        tag = self.request.GET.get("tag", "")

        context["search_form"] = NoteGroupSearchForm(
            initial={"name": name}
        )
        context["filter_form"] = TechTagFilterForm(
            initial={"tag": tag}
        )
        return context


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
