from django.urls import path

from users import views

urlpatterns = [
    path("register/", views.registration, name="sign-up"),
    path(
        "profile/<int:pk>/",
        views.TechUserDetailView.as_view(),
        name="profile"
    ),
    path(
        "profile/<int:pk>/update/",
        views.TechUserUpdateView.as_view(),
        name="profile-update"
    ),
    path(
        "profile/<int:pk>/delete/",
        views.TechUserDeleteView.as_view(),
        name="profile-delete"
    ),
]

app_name = "users"
