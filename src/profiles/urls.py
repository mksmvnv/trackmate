from django.urls import path

from . import views
from . import api_views

urlpatterns = [
    path("profiles/<int:id>/", views.ProfileView.as_view(), name="profile"),
    path(
        "profiles/<int:id>/update/",
        views.UpdateProfileView.as_view(),
        name="profile-update",
    ),
    path(
        "api/task-status/<int:user_id>/",
        api_views.TaskStatusDataView.as_view(),
        name="task-api-status",
    ),
]
