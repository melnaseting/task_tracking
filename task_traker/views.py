from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class TaskListView(ListView):
    model = models.Task
    template_name = 'task_traker/task_list.html'
    context_object_name = 'task_list'
    ordering = ["-created_date"]
