from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.TaskListView.as_view(), name='task_list'),
    path('add-task/',views.TaskCreateViev.as_view(), name='add_task'),
    path('<int:pk>/detales',views.TaskDetalesView.as_view(), name='task_detales'),
    path('<int:pk>/detales/add_comment',views.CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/detales/add-executer/<int:user_id>',views.TaskAddExecuterView.as_view(), name='task_add_executer'),
    path('<int:pk>/detales/update/',views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/detales/delete/',views.TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/complete/', views.TaskCompleteView.as_view(), name='task_complete'),

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
app_name="task_traker"