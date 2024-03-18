from django.test import TestCase

from note.models import TechTag
from users.forms import TechUserCreationForm, CouponForm


class TechUserCreationFormTest(TestCase):
    @staticmethod
    def get_form_data() -> dict:
        return {
            "username": "papajoe",
            "password1": "$ecreT_550",
            "password2": "$ecreT_550",
        }

    def test_tech_user_registration_form_valid_skill(self):
        form_data = self.get_form_data()
        form_data["skill"] = TechTag.objects.create(name="Plip")
        form = TechUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tech_user_creation_form_no_skill(self):
        form_data = self.get_form_data()
        form = TechUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class CouponFormValidationTest(TestCase):
    def test_coupon_form_valid_code(self):
        valid_coupon_codes = [
            "X1XX-342X-4564",
            "XXXX-XXXX-XXXX",
            "1111-2222-3333",
            "ADBS-34G5-FH6F",
        ]
        for coupon_code in valid_coupon_codes:
            form = CouponForm(data={"coupon_code": coupon_code})
            self.assertTrue(form.is_valid())

    def test_coupon_form_invalid_code(self):
        invalid_coupon_codes = [
            "XXX-342X-4564",
            "XXXX-XXXX",
            "1111-2222-3333-FYJ4",
            "ADBS34G5FH6F",
        ]
        for coupon_code in invalid_coupon_codes:
            form = CouponForm(data={"coupon_code": coupon_code})
            self.assertFalse(form.is_valid())
