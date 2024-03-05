from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import TechUser


class TechUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = TechUser
        fields = UserCreationForm.Meta.fields + (
            "skill",
            "first_name",
            "last_name",
            "email",
        )


class TechUserUpdateForm(forms.ModelForm):
    class Meta:
        model = TechUser
        fields = (
            "username", "skill", "first_name", "last_name", "email",
        )
