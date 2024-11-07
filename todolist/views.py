from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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

class TaskDoneView(generic.TemplateView):
    model = Task
    fields = "done"
    success_url = reverse_lazy("todolist:index")
    template_name = "todolist/task_done.html"

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        task.is_done = not task.is_done
        task.save()
        return task


class TagListView(generic.ListView):
    model = Tag

