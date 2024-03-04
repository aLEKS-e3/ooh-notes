from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from note.models import TechTag


class TechUser(AbstractUser):
    skill = models.ForeignKey(
        to=TechTag,
        on_delete=models.DO_NOTHING,
        related_name="tech_users",
    )

    class Meta:
        ordering = ("username",)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def __str__(self):
        return self.username
