from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.TaskListView.as_view(), name='task_list'),
    
]