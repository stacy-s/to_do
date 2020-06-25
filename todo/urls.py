from django.urls import path
from .views import *


urlpatterns = [
    path('task/create/', TaskCreate.as_view(), name='task_create_url'),
    path('tasks/', TaskListView.as_view(), name='tasks_list_url'),
]

