from django.urls import path

from .views import (
    index,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDoneView,
)

urlpatterns = [
    path("", index, name="index"),
    path("/tag-list", TagListView.as_view(), name="tag-list"),
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
    path('task/done/<int:task_id>/',
         TaskDoneView.as_view(),
         name='task-done'
         )

]

app_name = "todolist"