from django.urls import path

from note import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.NoteListView.as_view(), name="note-list"),
    path(
        "notes/<int:pk>/",
        views.NoteDetailView.as_view(),
        name="note-detail"
    ),
    path(
        "notes/<int:pk>/update/",
        views.NoteUpdateView.as_view(),
        name="note-update"
    ),
    path(
        "notes/<int:pk>/delete/",
        views.NoteDeleteView.as_view(),
        name="note-delete"
    ),
    path("notes/create/", views.NoteCreateView.as_view(), name="note-create"),
]

app_name = "note"
