from django.urls import path

from .views import CreateTaskListView, UpdateTaskStatusView

urlpatterns = [
    path("", CreateTaskListView.as_view(), name="index"),
    path(
        "update_status/<int:pk>/", UpdateTaskStatusView.as_view(), name="update_status"
    ),
]
