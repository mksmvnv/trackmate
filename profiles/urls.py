from django.urls import path

from . import views

urlpatterns = [
    path("profiles/<int:id>/", views.ProfileView.as_view(), name="profile"),
    path(
        "profiles/edit/<int:id>/", views.EditProfileView.as_view(), name="edit-profile"
    ),
]
