from django.urls import path

from .views import (
    index,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "task_types/",
        TaskTypeListView.as_view(),
        name="task-type-list",
    ),
    path(
        "task_types/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create",
    ),
    path(
        "task_types/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "task_types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
]

app_name = "task_manager"
