from django.db import models
from django.contrib.auth import settings


class TechTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    resources = models.CharField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes"
    )
    tags = models.ManyToManyField(to=TechTag, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} by {self.owner}"
