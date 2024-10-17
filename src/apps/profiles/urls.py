from django.urls import path

from . import views
from . import api

urlpatterns = [
    path("profiles/<uuid:id>/", views.ProfileView.as_view(), name="profile"),
    path(
        "profiles/<uuid:id>/update/",
        views.UpdateProfileView.as_view(),
        name="profile-update",
    ),
    path(
        "api/task-status/<uuid:user_id>/",
        api.TaskStatusDataView.as_view(),
        name="task-api-status",
    ),
]
