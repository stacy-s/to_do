from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'comment', 'priority', ]
        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'comment': forms.TextInput(attrs={'class': 'form-control'}),
                    'priority': forms.Select(attrs={'class': 'form-control'}),
        }
