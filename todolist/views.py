from django.shortcuts import render

from todolist.models import Task


def index(request):
    task_list = Task.objects.all()
    return render(request, "todo/index.html", {"task_list": task_list})