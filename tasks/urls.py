from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("tasks/", views.CreateTaskListView.as_view(), name="tasks"),
    path(
        "tasks/update_status/<int:pk>/",
        views.UpdateTaskStatusView.as_view(),
        name="task-update-status",
    ),
    path("tasks/update/<int:pk>/", views.UpdateTaskView.as_view(), name="task-update"),
    path("tasks/delete/<int:pk>/", views.DeleteTaskView.as_view(), name="task-delete"),
]
