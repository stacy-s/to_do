from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import ListView
import django_tables2 as tables
from django.views.decorators.csrf import csrf_exempt
from django_tables2 import SingleTableView
from .tables import TasksTable

from .forms import *
# Create your views here.


class TaskCreate(View):
    template = 'todo/task_create_form.html'
    form_model = TaskForm

    @csrf_exempt
    def get(self, request):
        form = self.form_model(request.GET)
        return render(request, self.template, context={'form': form})

    @csrf_exempt
    def post(self, request):
        form = self.form_model(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creation_datetime = timezone.now()
            task.is_finished = False
            # task.author = request.user
            task.save()
            # return redirect(task)
            return render(request, self.template, context={'form': form})
        return render(request, self.template, context={'form': form})

# class TaskTable(View):
#     template = 'todo/task_list.html'
#
#     @csrf_exempt
#     def get(self, request):
#         tasks = Task.objects.all()
#         return render(request, self.template, context={'tasks': tasks})


class TaskListView(SingleTableView):
    model = Task
    table_class = TasksTable
    template_name = 'task_list.html'


# class TaskTableView(tables.SingleTableView):
#     table_class = TasksTable
#     queryset = Task.objects.all()
#     template_name = "task_list.html"
