import profile

from django.urls import path

from users import views

urlpatterns = [
    path("register/", views.registration, name="sign-up"),
    path("profile/<int:pk>/", views.TechUserDetailView.as_view(), name="profile")
]

app_name = "users"
