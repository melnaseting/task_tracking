from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.TaskListView.as_view(), name='task_list'),
    path('add-task/',views.TaskCreateViev.as_view(), name='add_task'),
    path('<int:pk>/detales',views.TaskDetalesView.as_view(), name='task_detales'),
    path('<int:pk>/complete/', views.TaskCompleteView.as_view(), name='task_complete'),
    path('<int:pk>/detales/update/',views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/detales/delete/',views.TaskDeleteView.as_view(), name='task_delete'),

    
]
app_name="task_traker"