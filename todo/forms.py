from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'comment', 'priority', 'deadline',]
        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'comment': forms.Textarea(attrs={'class': 'form-control'}),
                    'priority': forms.RadioSelect(attrs={'class': 'form-check'}),
                    'deadline': forms.SelectDateWidget(attrs={'class': 'form-row form-control'}),
        }
