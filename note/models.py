from django.db import models
from django.contrib.auth import settings
from django.urls import reverse


class TechTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    resources = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(TechTag)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        default_related_name = "notes"

    def get_absolute_url(self):
        return reverse("note:note-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.title} by {self.owner}"


class NoteGroup(models.Model):
    name = models.CharField(max_length=255)
    notes = models.ManyToManyField(Note)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    tag = models.ForeignKey(TechTag, on_delete=models.DO_NOTHING)

    class Meta:
        default_related_name = "note_groups"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("note:note-group-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.name} by {self.owner}"
