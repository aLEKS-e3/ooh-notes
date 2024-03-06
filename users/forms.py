from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

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


def validate_coupon_code(coupon_code_input: str):
    coupon_code = RegexValidator(
        regex=r"^[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$",
        message=(
            "Coupon code includes numbers and capital letters, "
            "and has a next format -> 'XXXX-XXXX-XXXX'"
        ),
        code="invalid_coupon_code"
    )
    coupon_code(coupon_code_input)


class CouponForm(forms.Form):
    coupon_code = forms.CharField(
        max_length=255,
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter a coupon code..."
            }
        ),
        validators=[validate_coupon_code]
    )
