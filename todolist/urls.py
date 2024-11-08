from django.urls import path

from todolist.views import (
    index,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDoneView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "task/update/<int:pk>/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/delete/<int:pk>/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/done/<int:pk>/",
        TaskDoneView.as_view(),
        name="task-done"
         ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tags"
    ),
    path(
        "tag/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tag/update/<str:name>/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tag/delete/<str:name>/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "todolist"
