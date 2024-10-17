from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("tasks/", views.CreateTaskListView.as_view(), name="tasks"),
    path(
        "tasks/<uuid:pk>/update_status/",
        views.UpdateTaskStatusView.as_view(),
        name="task-update-status",
    ),
    path("tasks/<uuid:pk>/update/", views.UpdateTaskView.as_view(), name="task-update"),
    path("tasks/<uuid:pk>/delete/", views.DeleteTaskView.as_view(), name="task-delete"),
]
