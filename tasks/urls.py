from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateTaskListView.as_view(), name="index"),
    path(
        "update_status/<int:pk>/",
        views.UpdateTaskStatusView.as_view(),
        name="task-update-status",
    ),
    path("update/<int:pk>/", views.UpdateTaskView.as_view(), name="task-update"),
    path("delete/<int:pk>/", views.DeleteTaskView.as_view(), name="task-delete"),
]
