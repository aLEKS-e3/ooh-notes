from django.contrib.auth.forms import UserCreationForm

from users.models import TechUser


class TechUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = TechUser
        fields = UserCreationForm.Meta.fields + (
            "skill",
            "first_name",
            "last_name",
        )
