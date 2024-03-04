from django.urls import path

from users.views import registration

urlpatterns = [
    path("register/", registration, name="sign-up"),
]

app_name = "users"
