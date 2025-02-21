from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView , View , UpdateView, DeleteView
from  .mixins import UserIsOwnerMixin
from django.http import HttpResponseRedirect
from . import models,forms
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
    model = models.Task
    template_name = 'task_traker/task_list.html'
    context_object_name = 'task_list'
    ordering = '-created_date'
    
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(Q(created_by=self.request.user)|Q(executers=self.request.user))

        status = self.request.GET.get("status","")
        priority = self.request.GET.get("priority","")
        if status!="all" and priority!='all':
            queryset = queryset.filter(status=status,priority=priority)
        elif status=="all" and priority!='all':
            queryset = queryset.filter(priority=priority)
        elif priority=="all" and status!="all":
            queryset = queryset.filter(status=status)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.TaskFilterForm(self.request.GET)
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"]= User.objects.all()
        context["comments"] = models.Comment.objects.filter(task__pk = context["task"].pk)
        context["form"] = forms.CommentForm()
        return context

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = models.Comment()
    def post(self, request, *args, **kwargs):
        comment = models.Comment.objects.create(
            text = request.POST['text'],
            author = request.user,
            task = models.Task.objects.get(pk = kwargs['pk']))           
        return HttpResponseRedirect(reverse("task_traker:task_detales",args=[comment.task.pk]))
            
class TaskAddExecuterView(LoginRequiredMixin,UserIsOwnerMixin,View):
    def post(self,request , *args , **kwargs):
        task = self.get_object()
        executer = User.objects.get(id = kwargs.get('user_id'))
        if executer not in task.executers.all():
            task.executers.add(executer)
        else:
            task.executers.remove(executer)
        task.save()
        return HttpResponseRedirect(reverse("task_traker:task_detales",args=[task.pk]))
    
    def get_object(self): 
        task_id = self.kwargs.get('pk') 
        return get_object_or_404(models.Task, pk=task_id)

class TaskCompleteView(LoginRequiredMixin,UserIsOwnerMixin,View):
    def post(self,request , *args , **kwargs):
        task = self.get_object()
        task.status = 'done'
        task.save()
        return HttpResponseRedirect(reverse_lazy("task_traker:task_list"))
    
    def get_object(self): 
        task_id = self.kwargs.get('pk') 
        return get_object_or_404(models.Task, pk=task_id)
    
class TaskUpdateView(LoginRequiredMixin,UserIsOwnerMixin,UpdateView):
    model = models.Task
    template_name = 'task_traker/task_update_form.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy("task_traker:task_list")

class TaskDeleteView(LoginRequiredMixin,UserIsOwnerMixin,DeleteView):
    model = models.Task
    template_name = 'task_traker/task_delete.html'
    success_url = reverse_lazy("task_traker:task_list")
