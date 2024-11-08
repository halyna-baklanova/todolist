from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404

from todolist.models import Task, Tag


def index(request):
    task_list = Task.objects.all()
    return render(request, "todolist/index.html", {"task_list": task_list})


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist:index")


class TaskDoneView(generic.UpdateView):
    model = Task
    fields = ["done"]
    template_name = "todolist/task_done.html"

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        task.done = not task.done
        task.save()
        return task

    def get_success_url(self):
        return reverse_lazy("todolist:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todolist/tags.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tags")

    def get_object(self, queryset=None):
        return get_object_or_404(Tag, name=self.kwargs["name"])


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tags")

    def get_object(self, queryset=None):
        return get_object_or_404(Tag, name=self.kwargs["name"])
