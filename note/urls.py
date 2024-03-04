from django.urls import path

from note import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.NoteListView.as_view(), name="note-list"),
    path("notes/<int:pk>/", views.NoteDetailView.as_view(), name="note-detail"),
]

app_name = "note"
