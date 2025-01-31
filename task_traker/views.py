from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView , View , UpdateView, DeleteView
from  .mixins import UserIsOwnerMixin
from django.http import HttpResponseRedirect
from . import models,forms

# Create your views here.
class TaskListView(ListView):
    model = models.Task
    template_name = 'task_traker/task_list.html'
    context_object_name = 'task_list'
    ordering = ["-created_date"]

class TaskCreateViev(LoginRequiredMixin, CreateView):
    model = models.Task
    template_name = 'task_traker/task_form.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy("task_traker:task_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskDetalesView(DetailView):
    model = models.Task
    template_name = "task_traker/task_detales.html"
    context_object_name = "task"

class TaskCompleteView(LoginRequiredMixin,UserIsOwnerMixin,View):
    def post(self,request , *args , **kwargs):
        task = self.get_object()
        task.status = 'done'
        task.save()
        return HttpResponseRedirect(reverse_lazy("task_traker:task_list"))
    
    def get_object(self): 
        task_id = self.kwargs.get('pk') 
        return get_object_or_404(models. Task, pk=task_id)
    
class TaskUpdateView(LoginRequiredMixin,UserIsOwnerMixin,UpdateView):
    model = models.Task
    template_name = 'task_traker/task_update_form.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy("task_traker:task_list")

class TaskDeleteView(LoginRequiredMixin,UserIsOwnerMixin,DeleteView):
    model = models.Task
    template_name = 'task_traker/task_delete.html'
    success_url = reverse_lazy("task_traker:task_list")
