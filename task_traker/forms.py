from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','dead_line','priority','status']

    def __init__(self, *args, **kwargs): 
        super(TaskForm, self).__init__(*args, **kwargs) 
        self.fields["dead_line"].widget.attrs.update({"type": "datetime-local"})

class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('all','All'),
        ('to_do','To Do'),
        ('in_progress','In Progress'),
        ('done','Done')
    ]
    PRIORITY_CHOICES = [
        ('all','All'),
        ('low','Low'),
        ('medium',"Medium"),
        ('high',"High")
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES , label='Status')
    priority =forms.ChoiceField(choices=PRIORITY_CHOICES , label='Priority')

    def __init__(self, *args, **kwargs): 
        super(TaskFilterForm, self).__init__(*args, **kwargs) 
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-select form-select-m mb-3"}) 