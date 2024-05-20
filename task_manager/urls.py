from django.urls import path

from .views import (
    index,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    PositionListView,
    PositionDetailView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView
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
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "positions/<int:pk>/",
        PositionDetailView.as_view(),
        name="position-detail"
    ),

    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
    path(
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"
    ),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"
    ),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
]

app_name = "task_manager"
