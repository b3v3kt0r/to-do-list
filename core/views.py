from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "core/task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("core:task_list")
    template_name = "core/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("core:task_list")
    template_name = "core/task_form.html"


class TaskDeleteView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("core:task_list")
    template_name = "core/task_confirm_delete.html"


def check(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    if task.checker is True:
        task.checker = False
    else:
        task.checker = True
    task.save()
    return redirect(reverse_lazy("core:task_list"))


class TagsListView(generic.ListView):
    model = Tag
    template_name = "core/tags_list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tags_list")
    template_name = "core/tags_form.html"


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tags_list")
    template_name = "core/tags_form.html"


class TagsDeleteView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tags_list")
    template_name = "core/tags_confirm_delete.html"
