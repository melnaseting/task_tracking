from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('to_do','To Do'),
        ('in_progress','In Progress'),
        ('done','Done')
    ]
    PRIORITY_CHOICES = [
        ('low','Low'),
        ('medium',"Medium"),
        ('high',"High")
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    dead_line = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=20, default="medium",choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, default="to_do",choices=STATUS_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    executers = models.ManyToManyField(User,related_name='appointed_tasks', null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} created by {self.created_by}"
