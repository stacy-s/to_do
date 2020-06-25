import django_tables2 as tables
from .models import Task


class TasksTable(tables.Table):
    class Meta:
        model = Task
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-striped'}